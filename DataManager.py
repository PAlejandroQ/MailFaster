import json
from json.decoder import JSONDecodeError
class DataManager:
    def __init__(self) -> None:
        self.loadPersistentData()
        
    def initStructure(self):
        self.data = {}
        self.data["emails"] = []
        self.data["templates"] = {}
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
        newTemplate = {}
        newTemplate["name"] = nameTemplate
        newTemplate["body"] = body
        newTemplate["parameters"] = self.extractParameters(body)
        self.data["templates"] = newTemplate
        self.saveJson()
    def extractParameters(self, body : str) -> dict:
        return {}
    def addEmail(self, email : str):
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