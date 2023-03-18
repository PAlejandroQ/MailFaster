import smtplib
import ssl

class MailComunication:
    def __init__(self):
        self.context = ssl.create_default_context()
        self.serverData = {"gmail" : ["smtp.gmail.com",465], "outlook": ["smtp-mail.outlook.com",587]}
    def sendMail(self,mailMaker, email_password, server = "gmail"):
        with smtplib.SMTP_SSL(host= self.serverData[server][0], port = self.serverData[server][1], context=self.context) as smtp:
            smtp.login(mailMaker.email_sender, email_password)
            smtp.sendmail(mailMaker.email_sender, mailMaker.email_receiver, mailMaker.email.as_string())