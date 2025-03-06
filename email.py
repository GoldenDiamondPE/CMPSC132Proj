class email():
    def __init__(self, email, type):
        self.__email = email
        self.__type = type

    def setEmail(self, email):
        self.__email = email
    def setType(self, type):
        self.__type = type

    def getEmail(self):
        return self.__email
    def getType(self):
        return self.__type

    def __str__(self):
        return f"{self.__email} {self.__type}"