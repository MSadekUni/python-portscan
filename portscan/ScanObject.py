__all__ = [
    'ScanObject'
]


class ScanObject:
  def __init__(self):
    """Contructor of object containing a single nmap scan entity"""
    self.start_ip = self.subnet = self.range = self.ports = ""
    self.command = ""
    self.outfile = ""

  def GetMachineCount(self):
    """Determines the number of IP's that will be scanned with this object instance"""
    if self.subnet is None and self.range is None:
      return 1
    elif self.range is None:
      return pow(2, 32 - int(self.subnet))
    else:
      end = self.start_ip.split('.')[3]
      return int(self.range) - int(end) + 1

  def Populate(self, line):
    """From a given legal line of input, determine type of input for nmap"""
    
    isinstance(line, str)

    # Parse any individual ports
    if ':' in line:
      line = line.split(':')
      self.ports = line[1];
      # trim any trailing commas
      while self.ports[-1] == ',':
        self.ports = self.ports[:-1]
      line = line[0]
    else:
      self.ports = None

    # 1.2.3.0/24 - > 1.2.3.0 & 24
    if '/' in line:
      line = line.split('/')
      self.subnet = line[1]
      self.start_ip = line[0]
      self.range = None
    # 1.2.3.0-255 -> 1.2.3.0 & 255
    elif '-' in line:
      line = line.split('-')
      self.range = line[1]
      self.start_ip = line[0]
      self.subnet = None
    # 1.2.3.4 -> 1.2.3.4
    else:
      self.start_ip = line
      self.range = None
      self.subnet = None
    return True

  def CreateCommand(self, exclusion_string, global_ports, out_dir):
    """Takes input from the BusinessUnit object that owns this ScanObject and creates the command for the system to execute"""
    
    isinstance(exclusion_string, str)
    isinstance(global_ports, str)
    isinstance(out_dir, str)



    # THIS IS ALLOWED. CHECKS HAVE BEEN MADE, bad_ports 
    # will always have a single comma after. self.ports 
    # will never
    if self.ports is not None:
      total_ports = global_ports + self.ports
    else:
      total_ports = global_ports[:-1]

    self.outfile = out_dir + "nmap-T-" + self.start_ip + ".out"

    if len(exclusion_string) > 0 :
      exclude = "--exclude " + exclusion_string[:-1]
    else:
      exclude = ""

    if self.subnet is None and self.range is None:
      key = self.start_ip
    elif self.subnet is None:
      key = self.start_ip + "-" + self.range
    else:
      key = self.start_ip + "/" + self.subnet

    self.command = "nmap -P0 -sT -p " + total_ports + " -oX " + self.outfile \
      + " " + exclude + " " + key + " > /dev/null 2>&1"




