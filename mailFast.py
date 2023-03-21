from MailMaker import  MailMaker
from MailComunication import MailComunication
from getSecret import GetSecret
from gui import GUI
from tkinter import BOTTOM
# getSecret = GetSecret()
# getSecret.readFile("secret.txt")
# email_sender = getSecret.getLine(2)
# email_password = getSecret.getLine(3)
# email_receiver = getSecret.getLine(4)

# subject = 'Dinamic Mail from GUI!'
body = """
GUI test send.
"""
def sendEmail():
    mailMaker = MailMaker()
    
    mailMaker.autoSetJson(gui.getDataJson())
    mailMaker.setMesage(body)

    mailComunication = MailComunication()
    mailComunication.sendMail(mailMaker,gui.dataForm['Password'], server="outlook")

gui = GUI()
gui.addTextBox("From")
options = [("Uno","U"),("Multiple","M"),("Grupo","G")]
gui.addRadioButton("To", options, initValue="U")
gui.addTextBox("Subject")
gui.addButton("Salir",gui.exit())
gui.addButton("Enviar",sendEmail)
gui.addTextBox("Password", passSim="*" ,sideTbx=BOTTOM)
gui.addButton("Preview",gui.exit())
gui.addTextBoxBody()
gui.addComboBox("Templates",gui.getTemplates(),BOTTOM, isTrace=True)
gui.setMainLoop()



# mailMaker = MailMaker()
# mailMaker.setSender(email_sender)
# mailMaker.setRecivers(email_receiver)
# mailMaker.setSubject(subject)
# mailMaker.setMesage(body)

# mailComunication = MailComunication()
# mailComunication.sendMail(mailMaker,email_password, server="outlook")






class controllerApp:
    def __init__(self):
        # Add check if is Online
        pass
    
class templatesMail:
    pass