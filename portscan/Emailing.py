import arrow
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os

__all__ = [
    'SendMail',
]


def SendMail(BU, server="localhost"):
    """Send formatted email using information from a BuisnessUnit Object."""

    # Timestamp init
    utc = arrow.utcnow()
    local = utc.to('US/Pacific')

    htmlFile = BU.nmap_dir + "out.html" 

    # Subject Creation
    subject = "Scan-" + local.format('YYYY-MM-DD HH:mm:ss')

    if BU.verbose != "":
        subject = BU.verbose + " " + subject

    if BU.stats["open"] > 0 or BU.stats["open|filtered"] > 0:
        subject = "ACTION REQUIRED-" + subject

    if BU.org != "":
        subject = BU.org + "-" + subject

    
    #if len(BU.mobile) > 0:
    #    emailList = [BU.emails, BU.mobile]
    #else:
    emailList = [BU.emails]
        
    
        
    for i in range(0,len(emailList)):
        msg = MIMEMultipart()
        msg['From'] = "Scanner@KaliBox.com"
        msg['To'] = COMMASPACE.join(emailList[i])
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        
        with open(htmlFile, 'r') as myfile:
            data = myfile.read()
        msg.attach(MIMEText(data, 'html'))

        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(htmlFile,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                % os.path.basename(htmlFile))
        msg.attach(part)
        try:
            smtp = smtplib.SMTP(server)
            smtp.sendmail("Scanner@KaliBox.com", emailList[i], msg.as_string() )
            smtp.close()
            print("Successfully sent mail")
        except smtplib.SMTPException as e:
            print("Error: unable to send email")
            print(e)

