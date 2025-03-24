# CMPSC132
# Brandon and Gabe
# 3/24/2025
# This gathers the preferred method of contact via email of the student.

class email():
    def __init__(self, email, typeOfEmail):
        self.__email = email
        self.__typeOfEmail = typeOfEmail

    def setEmail(self, email):
        self.__email = email
    def settypeOfEmail(self, typeOfEmail):
        self.__typeOfEmail = typeOfEmail

    def getEmail(self):
        return self.__email
    def gettypeOfEmail(self):
        return self.__typeOfEmail

    def __str__(self):
        return f"{self.__email}, {self.__typeOfEmail}"