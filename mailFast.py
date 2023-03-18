from MailMaker import  MailMaker
from MailComunication import MailComunication
from getSecret import GetSecret

getSecret = GetSecret()
getSecret.readFile("secret.txt")
email_sender = getSecret.getLine(0)
email_password = getSecret.getLine(1)
email_receiver = getSecret.getLine(4)

subject = 'Correo dinamico!'
body = """
Testeando conexiones.
READY
"""

mailMaker = MailMaker()
mailMaker.setSender(email_sender)
mailMaker.setRecivers(email_receiver)
mailMaker.setSubject(subject)
mailMaker.setMesage(body)

mailComunication = MailComunication()
mailComunication.sendMail(mailMaker,email_password)






class controllerApp:
    def __init__():
        # Add check if is Online
        pass
    
class templatesMail:
    pass