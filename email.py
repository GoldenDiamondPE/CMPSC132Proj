class email():
    def __init__(self, email, type):
        self.__number = email
        self.__type = type

    def setNumber(self, number):
        self.__number = number
    def setType(self, type):
        self.__type = type

    def getNumber(self):
        return self.__number
    def getType(self):
        return self.__type