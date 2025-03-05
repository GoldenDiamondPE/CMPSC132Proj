class address():
    def __init__(self, streetNumber, street,  city, state,  zipCode):
        self.__streetNumber = streetNumber
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipCode = zipCode

    def setstreetNumber(self, streetNumber):
        self.__streetNumber = streetNumber
    def setStreet(self, street):
        self.__street = street
    def setCity(self, city):
        self.__city = city
    def setState(self, state):
        self.__state = state
    def setZipCode(self, zipCode):
        self.__zipCode = zipCode

    def getstreetNumber(self):
        return self.__streetNumber
    def getStreet(self):
        return self.__street
    def getCity(self):
        return self.__city
    def getState(self):
        return self.__state
    def getZipCode(self):
        return self.__zipCode
