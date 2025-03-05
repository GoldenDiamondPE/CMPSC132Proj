class nameOfStudent(Student):
    def __init__(self, firstName, middleName, lastName):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName

    def setFirstName(self, firstName):
        self.firstName = firstName
    def setMiddleName(self, middleName):
        self.middleName = middleName
    def setLastName(self, lastName):
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName
    def getMiddleName(self):
        return self.middleName
    def getLastName(self):
        return self.lastName