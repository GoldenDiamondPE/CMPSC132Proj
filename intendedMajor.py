class intendedMajor():
    def __init__(self, intendedMajor):
        self.__intendedMajor = intendedMajor

    def setIntendedMajor(self, intendedMajor):
        self.__intendedMajor = intendedMajor

    def getIntendedMajor(self):
        return self.__intendedMajor

    def __str__(self):
        return self.__intendedMajor