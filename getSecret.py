class GetSecret:
    def __init__(self) -> None:
        self.data = []
    def readFile(self,filename):
        with open(filename, 'r') as file:
            for line in file:
                self.data.append(line.rstrip('\n'))
    def getLine(self,nLine:int):
        return self.data[nLine]
