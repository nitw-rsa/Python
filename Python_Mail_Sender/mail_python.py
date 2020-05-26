'''
Author: Rishabh Sharma
'''

import smtplib
from email.mime.text import MIMEText

mail_message = """<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>
<body>
<h2>This is testing mail</h2>
<h2>This is my mail</h2>
<p>Please work on these items</p>
<table>
  <tr>
    <th>Task-1</th>
    <th>Task-2</th>
    <th>Task-3</th>
  </tr>
  </body>
  </html>"""

org_message = "Hi " + "Rishabh Sharma" + ", <br/><br/></br/>"
org_message += mail_message
org_message = org_message.replace('"', '')

smtp_ssl_host = "smtp.gmail.com"
smtp_ssl_port = 587
username = "rishabh@gmail.com"
password = "testing"
sender = "testing@gmail.com"
rec_mail = "testing1@gmail.com"
targets = [rec_mail]
cc_targets_list = []

msg = MIMEText(org_message, "html")
msg["Subject"] = "This is the mail subject"
msg["From"] = sender
msg["To"] = ", ".join(targets)
msg["Cc"] = ", ".join(cc_targets_list)

server = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
# server.login(username, password)
server.sendmail(sender, [targets] + cc_targets_list, msg.as_string())
server.quit()

print("Mail sent")
