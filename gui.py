from tkinter import  *
from tkinter import ttk
import json
# Password at the end for security
fields = ('From', 'To', 'CC','CCO')
class GUI:
    def __init__(self):
        self.window = Tk()
        self.dataForm = {}
        self.dataJson = {}
        self.lastObject = None
    def addTextBox(self,field, passSim = None):
        row = Frame(self.window)
        lbl = Label(row, width=22, text=field+": ", anchor='w')
        tbx = Entry(row,show=passSim)
        tbx.insert(0,"Escribe aqui...")
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        lbl.pack(side = LEFT)
        tbx.pack(side = RIGHT, expand = YES, fill = X)
        self.dataForm[field] = tbx
    def addRadioButton(self,field,radio_options:list, initValue = None):
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
        self.dataForm[field] = radioVar
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
    def addComboBox(self, field, values):
        var = StringVar()
        row = Frame(self.window)
        # lbl = Label(row, width=22, text=field+": ", anchor='w')
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        # lbl.pack(side = LEFT)
        comboBox = ttk.Combobox(row, values = values, textvariable = var)
        comboBox.current(0)
        comboBox.pack(side = RIGHT, expand = YES, fill = X)
        
        self.dataForm[field] = comboBox
        self.lastObject = row
    def getDataJson(self,e):
        for key in e.keys():
            if isinstance(e[key],Entry):
                self.dataJson[key] = e[key].get()
            if isinstance(e[key],StringVar):
                self.dataJson[key] = e[key].get()
            if isinstance(e[key],Listbox):
                self.dataJson[key] = [e[key].get(i) for i in e[key].curselection()]
            if isinstance(e[key],ttk.ComboBox):
                self.dataJson[key] = e[key].get()
            else:
                print("REVISAR OBJETOS GUARDADOS!!!")
        print(self.dataJson)
        self.saveJson(self.dataJson[list(self.dataJson.keys())[0]], self.dataJson)
    def saveJson(self, filename,data):
        with open(filename + ".json", 'w') as f:
            json.dump(data,f)
    def setMainLoop(self):
        self.window.mainloop()
    def updateGui(self):
        if self.lastRbtVar.get() == "U":
            self.clearLastObject()
            self.addComboBox("ToCbx", self.getEmails())
        elif self.lastRbtVar.get() == "M":
            self.clearLastObject()
            self.addListBox("ToLbx", self.getEmails())
        elif self.lastRbtVar.get() == "G":
            self.clearLastObject()
            self.addListBox("ToLbx", self.getEmails(True))
        else:
            print("NO SE ESTA DETECTANDO EL CAMBIO DEL RADIOBUTTOM!!!")
    def getEmails(self, asGroup=False):
        if asGroup:
            listOptions = ["Grupo Azul", "Equipo Rojo"]
        else:
            listOptions = ["example1@gmail.com","example2@gmail.com"]
        return listOptions
    def clearLastObject(self):
        if self.lastObject is not None:
            self.lastObject.pack_forget()

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