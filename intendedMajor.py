# CMPSC132
# Brandon and Gabe
# 3/24/2025
# This has the class Intended Major to find out what major the student is aiming for

class intendedMajor():
    def __init__(self, intendedMajor):
        self.__intendedMajor = intendedMajor

    def setIntendedMajor(self, intendedMajor):
        self.__intendedMajor = intendedMajor

    def getIntendedMajor(self):
        return self.__intendedMajor

    def __str__(self):
        return self.__intendedMajor