class birthDate():
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def setYear(self, year):
        self.__year = year
    def setMonth(self, month):
        self.__month = month
    def setDay(self, day):
        self.__day = day

    def getYear(self):
        return self.__year
    def getMonth(self):
        return self.__month
    def getDay(self):
        return self.__day
