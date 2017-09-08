from . import Log

import arrow
from yattag import Doc
from yattag import indent
import fileinput


__all__ = [
    'GenerateHTML'
]


def GenerateHTML(BU):
  """ Programmatically Generates HTML using data served from a BusinessUnit object. """
  utc = arrow.utcnow()
  local = utc.to('US/Pacific')


  Log.send_log("Generating HTML output for " + BU.business_unit)


  doc, tag, text = Doc().tagtext()

  js = """
  function myFunction(inputID, hopefullyString) {
        // console.log(hopefullyString)
        var input, filter, table, tr, td, i;
        input = document.getElementById(hopefullyString);
        filter = input.value.toUpperCase();
        // filter = input.value;
        console.log("FILTER:" + filter)
        table = document.getElementById("myTable");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
          td = tr[i].getElementsByTagName("td")[inputID];
          if (td) {
            // console.log("evaluates to:" + td.innerHTML)
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
            } else {
              tr[i].style.display = "none";
            }
          }
        }
      }
  """


  with tag('html'):
    with tag('head'):
      with tag('title'):
        text('Something output')



    with tag('body'):
      with tag('script'):
        text(js)
      with tag('div', id="first", style="width: 300px; float:left; border: 1px solid black;"):
        with tag('h1', style="margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"):
          text('Nmap Scan Report')
        with tag('p', style="margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"):
          text(BU.verbose + " Scan")
        with tag('p', style="margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"):
          text(BU.org)
        with tag('p', style="margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"):
          text(str(BU.live_host) + "/" + str(BU.machine_count) + " items Up")
        with tag('p', style="margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"):
          text(local.format('YYYY-MM-DD HH:mm:ss'))
        with tag('p', style="text-decoration: underline; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"):
          text("Stats")
        with tag('p', style="margin-left: 40px; padding:0px; margin-top: 0px; margin-bottom: 0px;"):
          text("Open: " + str(BU.stats["open"]))
        with tag('p', style="margin-left: 40px; padding:0px; margin-top: 0px; margin-bottom: 0px;"):
          text("Open | Filtered: " + str(BU.stats["open|filtered"]))
        with tag('p', style="margin-left: 40px; padding:0px; margin-top: 0px; margin-bottom: 0px;"):
          text("Filtered: " + str(BU.stats["filtered"]))
        with tag('p', style="margin-left: 40px; padding:0px; margin-top: 0px; margin-bottom: 0px;"):
          text("Closed | Filtered: " + str(BU.stats["closed|filtered"]))
        with tag('p', style="margin-left: 40px; padding:0px; margin-top: 0px; margin-bottom: 0px;"):
          text("Closed: " + str(BU.stats["closed"]))
        if len(BU.links) > 0:
            with tag('p', style="margin-left: 5px; padding:0px; margin-top: 0px; margin-bottom: 0px;"):
                text("Dropbox link:")
                for link in BU.links:
                    with tag('p', style="margin-left: 40px; padding:0px; margin-top: 0px; margin-bottom: 0px;"):
                        text(str(link))
      with tag('div', id="second", style="overflow: hidden;"):
        with tag('input', type="text", id="myInput5", onkeyup="myFunction(5, 'myInput4')", placeholder="*", title="Type in a name", style="width:35px; margin-left: 0px; margin-right: 0px; padding: 0px;"):
          pass
        with tag('input', type="text", id="myInput", onkeyup="myFunction(0, 'myInput')", placeholder="Search for IP..", title="Type in a name", style="width:100px; margin-left: 0px; margin-right: 0px; padding: 0px;"):
          pass
        with tag('input', type="text", id="myInput1", onkeyup="myFunction(1, 'myInput1')", placeholder="Search for Port..", title="Type in a name", style="width:100px; margin-left: 0px; margin-right: 0px; padding: 0px;"):
          pass
        with tag('input', type="text", id="myInput2", onkeyup="myFunction(2, 'myInput2')", placeholder="Search for Status..", title="Type in a name", style="width:100px; margin-left: 0px; margin-right: 0px; padding: 0px;"):
          pass
        with tag('input', type="text", id="myInput3", onkeyup="myFunction(3, 'myInput3')", placeholder="Search for Type..", title="Type in a name", style="width:100px; margin-left: 0px; margin-right: 0px; padding: 0px;"):
          pass
        with tag('input', type="text", id="myInput4", onkeyup="myFunction(4, 'myInput4')", placeholder="Search for Business..", title="Type in a name", style="width:100px; margin-left: 0px; margin-right: 0px; padding: 0px;"):
          pass



        with tag('table', border="1|0", id="myTable"):
          with tag('tr', klass="header"):
            with tag('th', style="width:35px;"):
              text('New')
            with tag('th', style="width:100px;"):
              text('IP')
            with tag('th', style="width:100px;"):
              text('Port')
            with tag('th', style="width:100px;"):
              text('Status')
            with tag('th', style="width:100px;"):
              text('Type')
            with tag('th', style="width:100px;"):
              text('Business')
          with open(BU.outfile, 'r') as f:
            for line in f:
              if "open" in line:
                test = line.split(',') 
                with tag('tr'):
                  with tag('td'):
                    text(test[5])
                  with tag('td'):
                    text(test[0])
                  with tag('td'):
                    text(test[1])
                  with tag('td'):
                    text(test[2])
                  with tag('td'):
                    text(test[3])
                  with tag('td'):
                    text(test[4])
          
  with open(BU.nmap_dir + 'out.html', 'w') as f:
    f.write(indent(doc.getvalue()))
  with open(BU.nmap_dir + 'out.html', 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write("<!DOCTYPE html>".rstrip('\r\n') + '\n' + content)

  with fileinput.FileInput(BU.nmap_dir + 'out.html', inplace=True) as file:
    for line in file:
      print(line.replace('&gt;', '>'), end='')
  with fileinput.FileInput(BU.nmap_dir + 'out.html', inplace=True) as file:
    for line in file:
      print(line.replace('&lt;', '<'), end='')
  Log.send_log("Finished generating HTML output for " + BU.business_unit)
