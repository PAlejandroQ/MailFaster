import smtplib
import ssl
from tkinter import Entry
from CustomException import CustomException
class MailComunication:
    def __init__(self):
        self.context = ssl.create_default_context()
        self.serverData = {"gmail" : ["smtp.gmail.com",465, self.context], "outlook": ["smtp.office365.com",587, None]}
    def sendMail(self,mailMaker, email_password, server = "gmail"):
        # Deben mantenerse seta separacion, porque cada servidor 
        # usa un metodo se HandShaking que requiere esta forma.
        if not isinstance(email_password,str):
            email_password =  str(self.getPassword(email_password)) #
        if server == "gmail":
            with smtplib.SMTP_SSL(host= self.serverData[server][0], port = self.serverData[server][1],context=self.context) as smtp:
                smtp.login(mailMaker.email_sender, email_password)
                smtp.sendmail(mailMaker.email_sender, mailMaker.email_receiver, mailMaker.email.as_string())
        elif server == "outlook":
            with smtplib.SMTP(host= self.serverData[server][0], port = self.serverData[server][1]) as smtp:
                smtp.ehlo()
                smtp.starttls(context=self.context)
                smtp.ehlo() 
                smtp.login(mailMaker.email_sender, email_password)
                smtp.sendmail(mailMaker.email_sender, mailMaker.email_receiver, mailMaker.email.as_string())
        else:
            raise CustomException("Especifique un servidor valido!!!")
    def getPassword(self, objectPass):
        if isinstance(objectPass,Entry):
            return objectPass.get()
