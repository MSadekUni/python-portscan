# User Defined Modules
from . import HTMLGenerator
from . import Log
from . import ScanObject

try:
  from . import Upload
except EnvironmentError:
  upload_bool = False
  

# Standard Library Modules
# from libnmap.parser import NmapParser
import libnmap.parser
import os


__all__ = [
    'BusinessUnit'
]

# Business Uni 
class BusinessUnit:
  def __init__(self, p_name, p_path, p_verbose = "", p_org = ""):
    """ BusinessUnit Class Constructor. """

    isinstance(p_name, str)
    isinstance(p_path, str)
    isinstance(p_verbose, str)
    isinstance(p_org, str)

    Log.send_log("Scan started on " + p_name)

    # Provided input population
    self.business_unit = p_name
    self.path = p_path
    self.verbose = p_verbose
    self.org = p_org

    # Object populates this when Reading configs
    self.machine_count = 0;
    self.live_host = 0
    self.exclude_string = ""
    self.emails = self.mobile = self.links = []
    self.scan_objs = []
    self.stats = {"open":0, "open|filtered":0, "filtered":0, "closed|filtered":0, "closed":0}

    # immediatley populated by checkDeps()
    self.config_dir = self.ports_file = self.ip_file = self.nmap_dir = self.ports = self.outfile = ""
    self.CheckDeps()

  # Check that all neccessary configuration dependancies exist  
  def CheckDeps(self):
    """ Private Method that depends on self.path existing in the object. """
    if self.path == "":
      Log.send_log("CheckDeps called on " + self.business_unit + " object but does not contain a self.path defined variable. ")
      exit(0)

    self.config_dir = self.path + "config/"
    self.CheckExist(self.config_dir)

    self.ports_file = self.config_dir + "ports_bad_" + self.business_unit
    self.CheckExist(self.ports_file)

    self.ip_file = self.config_dir + "ports_baseline_" + self.business_unit + ".conf"
    self.CheckExist(self.ip_file)

    # output directory
    self.nmap_dir = self.path + "nmap-" + self.business_unit + "/"
    if not os.path.exists(self.nmap_dir):
      Log.send_log(self.nmap_dir + " does not exist... creating now")
      os.system("mkdir " + self.nmap_dir)

  def CheckExist(self, file):
    isinstance(file, str)
    """ Helper private method for CheckDeps """
    if not os.path.exists(file):
      print(file + " does not exist. Exiting...")
      Log.send_log(file+ " does not exist.")
      exit(0)

  def ReadPorts(self):
    """ Parse and store general ports from ports_bad_{business_unit}."""
    try:
      with open(self.ports_file, 'r') as f:
        for line in f:

          # Comment removal
          if line[0] == '#':
            continue
          elif '#' in line:
            line = line.split('#')[0]

          self.ports = self.ports + line.strip(' \t\n\r')
          
          # trim any trailing commas and add ONLY one
          # IMPORTANT. DO NOT REMOVE; SANITIZES USER INPUT
          while self.ports[-1] == ',':
            self.ports = self.ports[:-1]
          self.ports = self.ports + ','

    except IOError:
      Log.send_log("Unable to open " + self.ports_file)
      exit(1)
    Log.send_log("Finished reading ports")


  def ReadBase(self):
    """ Parse and store networks, subnets, ranges, and individual IP's for scanning from ports_baseline_{business_unit}.conf."""
    try:
      with open(self.ip_file, 'r') as f:
        for line in f:
          # test if line is empty and continue is so
          try:
            line.strip(' \t\n\r')[0]
          except:
            continue

          # Comments and emails
          if line[0] == '#':
            continue
          elif '#' in line:
            line = line.split('#')[0]
          elif '@' in line:
            if "-m" in line:
              self.mobile.append(line.split(' ')[0].strip(' \t\n\r'))
            else:
              self.emails.append(line.strip(' \t\n\r'))
            continue

          # Business unit scan object
          if line[0] == "-":
            self.exclude_string = self.exclude_string + line[1:].strip(' \t\n\r') + ","
            continue
          else:
            # create scan object
            BU_SO = ScanObject.ScanObject()
            # populate fields based on line input
            BU_SO.CreateCommand(line.strip(' \t\n\r'), self.exclude_string, self.ports, self.nmap_dir)
            self.scan_objs.append(BU_SO)
            self.machine_count = self.machine_count + BU_SO.GetMachineCount()
    except IOError:
      Log.send_log("Unable to open " + self.ip_file)
      exit(1)
    Log.send_log("Finished reading Commands")

  def Scan(self):
    """Execute scanning commands held in ScanObjects. Uses forking and waits on PID returns."""
    pids = []
    for obj in self.scan_objs:
      pid = os.fork()
      if pid != 0:
        pids.append(pid)
      else:
        Log.send_log(obj.command)
        os.system(obj.command)
        exit(0)
    for i in pids:
      os.waitpid(i, 0)


  def ParseOutput(self, buisness_path = ""):
    """Parse and assemble human readable csv report of all nmap results. """
    if len(buisness_path) > 0:
      master_dict = {}
      with open(buisness_path, "r") as f:
        for line in f:
          test = line.strip(' \n\t\r')
          test = test.split(',')
          master_dict[test[1]] = test[0]
      f.close() 

    master_out = []



    try:
      with open(self.nmap_dir + "output-" + self.business_unit + ".bak") as f:
        last = f.readlines()
      f.close()
    except IOError:
      last = []



    for obj in self.scan_objs:
      nmap_report = libnmap.parser.NmapParser.parse_fromfile(obj.outfile)
      for scanned_hosts in nmap_report.hosts:
          if scanned_hosts.is_up():
              self.live_host = self.live_host + 1
          for port in scanned_hosts.get_ports():
              nmap_obj = scanned_hosts.get_service(port[0], "tcp")
              if nmap_obj.state == "open" or nmap_obj.state == "open|filtered":
                out = [scanned_hosts.address, str(nmap_obj.port), nmap_obj.state, nmap_obj.service]
                

                # append business type
                if len(buisness_path) > 0:
                  out.append(master_dict.get(scanned_hosts.address, "") + "")
                else:
                  out.append("")
                
                # append new or not
                if len(last) > 0:
                  if len([s for s in last if ",".join(out) in s]) == 0:
                    out.append("*")
                  else:
                    out.append("")
                else:
                  out.append("*")

                master_out.append(",".join(out))

      
                self.stats[nmap_obj.state] = self.stats[nmap_obj.state] + 1
              else:
                self.stats[nmap_obj.state] = self.stats[nmap_obj.state] + 1
      Log.send_log("File " + obj.outfile + " parsed.")
    return master_out


  def Collect(self, buisness_path=""):
    """ Calls ParseOutput to collect all output into a readable csv. Generates HTML Generation and Uploading to DropBox. """
    isinstance(buisness_path, str)



    out = self.ParseOutput(buisness_path)
    self.outfile = self.nmap_dir + "output-" + self.business_unit + ".csv";

    try:
      os.system("cp " + self.outfile + " " + self.nmap_dir + "output-" + self.business_unit + ".bak")
    except:
      pass

    with open(self.outfile, 'w') as f:
      for line in out:
        f.write(line + "\n")

    Log.send_log("Generated CSV report.")
    # upload Report to DropBox
    try:
      self.links = Upload.UploadToDropbox([self.outfile], '/' + os.path.basename(os.path.normpath(self.nmap_dir)) + '/')
    except EnvironmentError:
        self.links = []
    # Generate HMTL
    HTMLGenerator.GenerateHTML(self)


    

if __name__ == "__main__":
  upload_bool = True
