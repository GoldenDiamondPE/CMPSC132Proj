# CMPSC132
# Brandon and Gabe
# 3/24/2025
# This program gathers the type and number the student prefers to be contacted from.

class phoneNumber():
    def __init__(self, number, type):
        self.__number = number
        self.__type = type

    def setNumber(self, number):
        self.__number = number
    def setType(self, type):
        self.__type = type

    def getNumber(self):
        return self.__number
    def getType(self):
        return self.__type

    def __str__(self):
        return f"{self.__number} {self.__type}"