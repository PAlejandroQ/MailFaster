import json
from json.decoder import JSONDecodeError
class DataManager:
    def __init__(self) -> None:
        self.loadPersistentData()
        
    def initStructure(self):
        self.data = {}
        self.data["emails"] = []
        self.data["templates"] = []
        self.data["groups"] = {}
        self.saveJson()
    def loadPersistentData(self,filename = "dataMailFast"):
        self.filenameData = filename
        try:
            with open(self.filenameData +'.json', 'r') as f:
                self.data = json.load(f)
        except JSONDecodeError:
            self.initStructure()
    def addTemplate(self, nameTemplate : str, body :str):
        if len(nameTemplate)<=1 or len(body)<=1:
            return
        newTemplate = {}
        newTemplate["name"] = nameTemplate
        newTemplate["body"] = body
        newTemplate["parameters"] = self.extractParameters(body)
        index = self.alreadyExist(nameTemplate)
        if index == -1:
            self.data["templates"].append(newTemplate)
        else:
            self.data["templates"][index] = newTemplate
        self.saveJson()
    def alreadyExist(self, nameItem, typeItem = "Template") -> int:
        for di in self.data["templates"]:
                if di["name"] == nameItem:
                    return self.data["templates"].index(di)
        return -1
    def extractParameters(self, body : str) -> dict:
        words = body.split()
        parameters = {}
        for word in words:
            if word.startswith('$'):
                parameters[word] = ""
        return parameters
    def addEmail(self, email : str):
        if len(email)<=1:
            return
        self.data["emails"].append(email)
        self.saveJson()
    def addGroup(self, groupName : str, emails : list):
        newGroup = {}
        newGroup[groupName] = emails
        self.data["groups"] = newGroup
        self.saveJson()
    def saveJson(self):
        with open(self.filenameData + ".json", 'w') as f:
            json.dump(self.data,f)
    # def setDefaultValues(self):
    #     pass
    

# usar listBox para seleccionar variables
# y asi editar sus valores con un mismo
# textBox de entrada    