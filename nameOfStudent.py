class nameOfStudent():
    def __init__(self, firstName, middleName, lastName):
        self.__firstName = firstName
        self.__middleName = middleName
        self.__lastName = lastName

    def setFirstName(self, firstName):
        self.__firstName = firstName
    def setMiddleName(self, middleName):
        self.__middleName = middleName
    def setLastName(self, lastName):
        self.__lastName = lastName

    def getFirstName(self):
        return self.__firstName
    def getMiddleName(self):
        return self.__middleName
    def getLastName(self):
        return self.__lastName