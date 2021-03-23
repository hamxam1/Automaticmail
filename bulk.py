import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

sender_email = "urmail@gmail.com"
receiver_email = ['recievers@mail.com']
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Sample Mail"
message["From"] = formataddr((str(Header('See so many receivers attached', 'utf-8')), 'sender@gmail.com'))
message["To"] = ", ".join(receiver_email)

# Create the plain-text and HTML version of your message
text = """\
"""
html = """\
<html>
   <div style="text-align:center;"><u><b> “Please use Google Chrome as the preferred internet browser.”<b></u></div>

       <br>
  <body>
    <b> Dear CSE (Customer Success Executive) Learners: </b> <br>
     <p> This is a notification reminder to complete the <a href="https://degreed.com/plan/315387#/"> Refreshed CSE Green Belt Training</a>
      by no later than end of Q3, April 30, 2021.  If you get started now, you should be able to easily achieve this prior to the target date.<br>
      <br>
     If you have any questions, please go to the <a href = "https://app.smartsheet.com/b/home?lgt=wf&lrt=s&EQBCT=092ed9bdd49249c2aee213cc884b1907"> 
      Success Academy Feedback Tracker </a> <br>
      <br>
      Your direct CSE POCs: <br>
     <b> Community Leader:</b> Ajay Tank (ajtank) <br>
     <b> Program Manager:</b> Deniz Saglik (desaglik)<br>
      <br>
      
      <b> Dear Managers: </b> <br>
    <p>To view your team’s CSE Training completion status, please click here to access your
    <a href = "https://tableau.cisco.com/#/site/CustomerExperienceLearning/views/LMExecutiveSummary/LMExecutiveSummary?:iid=1"> 
    Success Academy Tableau Dashboard </a><br>
    Please reference the <a href = "https://cisco.sharepoint.com/:p:/r/sites/CXEnablementGlobalHome/_layouts/15/guestaccess.aspx?e=pPf0vA&wdLOR=cA9C5437B-E4C6-5B42-A3A5-5BCE1B1E9030&share=EUiHfwL5tENNnCW53NsgOvgBy80VYYS_Vw40MBBQqUXuQg">
     DevCX Tableau Dashboard - Role Guide </a> for more detailed Tableau Reporting questions. </p>
     <br>
    
     
     Thank you, <br>
     Success Academy Team
     
    
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message032
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )