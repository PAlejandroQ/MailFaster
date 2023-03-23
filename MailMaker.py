import smtplib
import ssl
from email.message import EmailMessage
from CustomException import CustomException

class MailMaker:
    def __init__(self):
        self.email = EmailMessage()
    def setSender(self,email_sender):
        self.email['From'] = email_sender
        self.email_sender = email_sender
    def setRecivers(self, email_receiver):
        # email_receiver = self.formatAddress(email_receiver)
        self.email['To'] = email_receiver
        self.email_receiver = email_receiver
    def setCC(self,email_CCs):
        # email_CCs = self.formatAddress(email_CCs)
        self.email['Cc'] = email_CCs
    def setCCO(self, email_CCO):
        # email_CCO = self.formatAddress(email_CCO)
        self.email['Bcc'] = email_CCO
    def setSubject(self, subject):
        self.email['Subject'] = subject
    def setMesage(self,mesaggeBody):
        self.email.set_content(mesaggeBody)
    def formatAddress(self, listAddress) -> str:
        if isinstance(listAddress, list):
            print(listAddress)
            temp = ', '.join(listAddress)
            print(temp)
            return temp
        elif isinstance(listAddress, str):
            return listAddress
        else:
            raise CustomException("Input of adress is not list or string")
    def autoSetJson(self, jsonData):
        for key in jsonData.keys():
            if key == 'From':
                self.setSender(jsonData[key])
            elif key == 'To':
                self.setRecivers(jsonData[key])
            elif key == 'Subject':
                self.setSubject(jsonData[key])
            elif key == 'Body':
                self.setMesage(jsonData[key])
    

