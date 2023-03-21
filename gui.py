from tkinter import  StringVar, Frame, Label, Tk, Entry, \
TOP, LEFT, RIGHT, BOTTOM, X, YES, Radiobutton, Listbox, \
Button, ttk, END
import json
from CustomException import CustomException
from typing import Literal
from DataManager import DataManager

# Password at the end for security
fields = ('From', 'To', 'CC','CCO')
class GUI:
    def __init__(self):
        self.window = Tk()
        self.dataForm = {}
        self.dataJson = {}
        self.lastObject = None
        self.dataManager = DataManager()
    def addTextBox(self,field, passSim : str = "", sideTbx : Literal['left', 'right', 'top', 'bottom']  = TOP):
        row = Frame(self.window)
        lbl = Label(row, width=22, text=field+": ", anchor='w')
        tbx = Entry(row,show=passSim)
        tbx.insert(0,"Escriba aqui...")
        row.pack(side = sideTbx, fill = X, padx = 5, pady = 5)
        lbl.pack(side = LEFT)
        tbx.pack(side = RIGHT, expand = YES, fill = X)
        self.dataForm[field] = tbx
    def addTextBoxBody(self, sideTbx : Literal['left', 'right', 'top', 'bottom']  = BOTTOM, insertTxt = ""):
        row = Frame(self.window)
        tbx = Entry(row)
        tbx.insert(0,insertTxt)
        row.pack(side = sideTbx, fill = X, padx = 5, pady = 5)
        tbx.pack(side = RIGHT, expand = YES, fill = X)
        self.dataForm["Body"] = tbx
    def addRadioButton(self,field:str ,radio_options:list, initValue = None):
        # options = [("Uno","U"),("Multiple","M"),("Grupo","G")]
        radioVar = StringVar(value=initValue)
        row = Frame(self.window)
        lbl = Label(row, width=22, text=field+": ", anchor='w')
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        lbl.pack(side = LEFT)
        self.radioButtonList = {}
        for text, value in radio_options:
            Radiobutton(row, text=text, variable=radioVar, value=value, command=self.updateGui).pack(side=LEFT)
            # self.radioButtonList[text] = Radiobutton(row, text=text, variable=radioVar, value=value).pack(side=LEFT)
            # self.radioButtonList[text].pack(side = RIGHT)
        self.dataForm["Type"+field] = radioVar
        self.lastRbtVar = radioVar
        self.updateGui()
    def addListBox(self, field, listOptions):
        # listOptions = ["example@gmail.com","example2@gmail.com"]
        row = Frame(self.window)
        # lbl = Label(row, width=22, text=field+": ", anchor='w')
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        # lbl.pack(side = LEFT)
        listBox = Listbox(row, selectmode="multiple")
        for i, value in enumerate(listOptions,1):
            listBox.insert(i,value)
        listBox.pack(side = RIGHT, expand = YES, fill = X)
        self.dataForm[field] = listBox
        self.lastObject = row
    def addComboBox(self, field, values,sideCbx : Literal['left', 'right', 'top', 'bottom']  = TOP, isTrace = False):
        var = StringVar()
        row = Frame(self.window)
        # lbl = Label(row, width=22, text=field+": ", anchor='w')
        row.pack(side = sideCbx, fill = X, padx = 5, pady = 5)
        # lbl.pack(side = LEFT)
        comboBox = ttk.Combobox(row, values = values, textvariable = var)
        comboBox.pack(side = RIGHT, expand = YES, fill = X)
        
        self.dataForm[field] = comboBox
        if not isTrace:
            self.lastObject = row
        else:
            var.trace_add('write',self.updateGuiTemplate)
            self.varTracer = var

    def addButton(self, field, command):
        row = Frame(self.window)
        row.pack(side = BOTTOM, fill = X, padx = 5, pady = 5)
        button = Button(row, text = field, command=command)
        button.pack(side = RIGHT, expand = YES, fill = X)
        # self.dataForm[field] = button
        # self.lastObject = row

    def getDataJson(self):
        e = self.dataForm
        for key in e.keys():
            if isinstance(e[key],Entry) and key != 'Password':
                self.dataJson[key] = e[key].get()
            elif isinstance(e[key],StringVar):
                self.dataJson[key] = e[key].get()
            elif isinstance(e[key],Listbox):
                self.dataJson[key] = [e[key].get(i) for i in e[key].curselection()]
            elif isinstance(e[key],ttk.Combobox):
                self.dataJson[key] = e[key].get()
            # else:
            #     print(key)
            #     raise CustomException("REVISAR OBJETOS GUARDADOS!!!")
        # print(self.dataJson)
        self.saveJson(self.dataJson[list(self.dataJson.keys())[0]], self.dataJson)
        return self.dataJson
    def saveJson(self, filename,data):
        with open(filename + ".json", 'w') as f:
            json.dump(data,f)
    def setMainLoop(self):
        self.window.mainloop()
    def updateGui(self):
        if self.lastRbtVar.get() == "U":
            self.clearLastObject()
            self.addComboBox("To", self.getEmails())
        elif self.lastRbtVar.get() == "M":
            self.clearLastObject()
            self.addListBox("To", self.getEmails())
        elif self.lastRbtVar.get() == "G":
            self.clearLastObject()
            self.addListBox("To", self.getEmails(True))
        else:
            print("NO SE ESTA DETECTANDO EL CAMBIO DEL RADIOBUTTOM!!!")
    def getEmails(self, asGroup=False):
        if asGroup:
            listOptions = self.dataManager.data["groups"]
            # listOptions = ["Grupo Azul", "Equipo Rojo"]
        else:
            listOptions = self.dataManager.data["emails"]
            # listOptions = ["example1@gmail.com","example2@gmail.com"]
        return listOptions
    def getTemplates(self, getTemplate:str = "" ):
        if getTemplate == "":
            templatesNames = []
            for di in self.dataManager.data["templates"]:
                templatesNames.append(di["name"])
            return templatesNames
        else:
            for di in self.dataManager.data["templates"]:
                if di["name"] == getTemplate:
                    return di["body"]
    def clearLastObject(self):
        if self.lastObject is not None:
            self.lastObject.pack_forget()
    def exit(self):
        return self.window.quit
    def updateGuiTemplate(self,var, index, mode):
        print(self.varTracer.get())
        self.dataForm["Body"].delete(0, END)
        self.dataForm["Body"].insert(0,self.getTemplates(getTemplate= self.varTracer.get()))

def formMaker(window, fields):
    dataForm = {}
    for field in fields:
        row = Frame(window)
        lbl = Label(row, width=22, text=field+": ", anchor='w')
        tbx = Entry(row)
        tbx.insert(0,"0")
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        lbl.pack(side = LEFT)
        tbx.pack(side = RIGHT, expand = YES, fill = X)
        dataForm[field] = tbx
    return dataForm


def someFunction(e):
    pass

def calcular(e):
    dataJson = {}
    for key in e.keys():
        dataJson[key] = e[key].get()
    print(dataJson)
    saveJson(dataJson[list(dataJson.keys())[0]], dataJson)

def saveJson(filename,data):
    with open(filename + ".json", 'w') as f:
        json.dump(data,f)

if __name__=='__main__':
    window = Tk()
    window.title("Formulario")
    fields = ('Nombres', 'Apellidos', 'Correo', 'Telefono')
    dataForm = formMaker(window, fields)
    window.bind('<Return>',(lambda event, e = dataForm: someFunction(e)))
    b1 = Button(window, text="Guardar", command=(lambda e = dataForm: calcular(e)))
    b1.pack(side = LEFT, padx = 5,pady = 5)
    b2 = Button(window, text="Salir", command = window.quit)
    b2.pack(side = LEFT, padx = 5,pady = 5)
    window.mainloop()