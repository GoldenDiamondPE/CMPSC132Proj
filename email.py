class email():
    def __init__(self, email, type):
        self.number = email
        self.type = type

    def setNumber(self, number):
        self.number = number
    def setType(self, type):
        self.type = type

    def getNumber(self):
        return self.number
    def getType(self):
        return self.type