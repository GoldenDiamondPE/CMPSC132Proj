# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 4/24/2025
# Email nodes for the linked list

class EmailNode:
    def __init__(self, email):
        self.__email = email
        self.next = None

    def setStudentEmail(self, email):
        self.__email = email

    def getStudentEmail(self):
        return self.__email

    def __str__(self):
        return f"Node Data: {self.__email}\n"
