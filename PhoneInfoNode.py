# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 4/24/2025
# The phone node for the linked list

class PhoneNode:
    def __init__(self, phone):
        self.__phone = phone
        self.next = None

    def setStudentPhone(self, phone):
        self.__phone = phone

    def getStudentPhone(self):
        return self.__phone

    def __str__(self):
        return f"Node Data: {self.__phone}\n"
