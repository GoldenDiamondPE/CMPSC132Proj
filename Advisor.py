# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 4/24/2025
# Gets all the information regarding the Advisor and ties it with advisees

from AdviseesLinkedList import AdviseeLinkedList
from Student import Student

class Advisor:
    def __init__(self, firstName, lastName, middleName, title, department):
        self.__firstName = firstName
        self.__middleName = middleName
        self.__lastName = lastName
        self.__title = title
        self.__department = department
        self.__adviseeList = AdviseeLinkedList()

    # Getters
    def getFirstName(self):
        return self.__firstName
    def getMiddleName(self):
        return self.__middleName
    def getLastName(self):
        return self.__lastName
    def getTitle(self):
        return self.__title
    def getDepartment(self):
        return self.__department
    def getAdviseeList(self):
        return self.__adviseeList

    # Setters
    def setFirstName(self, firstName):
        self.__firstName = firstName
    def setMiddleName(self, middleName):
        self.__middleName = middleName
    def setLastName(self, lastName):
        self.__lastName = lastName
    def setTitle(self, title):
        self.__title = title
    def setDepartment(self, department):
        self.__department = department

    # Methods to edit advisee list
    def addAdvisee(self, studentID):
        self.__adviseeList.addAdvisee(studentID)

    def removeAdvisee(self, studentID):
        return self.__adviseeList.removeAdvisee(studentID)

    def __str__(self):
        return (f"Advisor Name: {self.__firstName} {self.__middleName} {self.__lastName}\n"
                f"Title: {self.__title}\n"
                f"Department: {self.__department}\n"
                f"Advisees: \n{self.__adviseeList}")
