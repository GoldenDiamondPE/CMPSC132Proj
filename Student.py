# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/24/2025
# This has the class Student to gather all the information regarding the student
# from name, ID, address, email, phone number, birthdate, acceptance date, start of semester, and intended Major

from CourseLinkedList import CourseLinkedList
from PhoneLinkedList import PhoneLinkedList
from Course import Course
from EmailLinkedList import EmailLinkedList

class Student():
    def __init__(self, name, ID, address, birthdate, acceptanceDate, semesterStart, intededMajor):
        self.name = name
        self.ID = ID
        self.address = address
        self.emailList = EmailLinkedList()
        self.phoneList = PhoneLinkedList()
        self.birthdate = birthdate
        self.acceptanceDate = acceptanceDate
        self.semesterStart = semesterStart
        self.intendedMajor = intededMajor
        self.courseList = CourseLinkedList()

    # Setters
    def setName(self, name):
        self.name = name
    def setID(self, ID):
        self.ID = ID
    def setAddress(self, address):
        self.address = address
    def setBirthdate(self, birthdate):
        self.birthdate = birthdate
    def setAcceptanceDate(self, acceptanceDate):
        self.acceptanceDate = acceptanceDate
    def setSemesterStart(self, semesterStart):
        self.semesterStart = semesterStart
    def setIntededMajor(self, intededMajor):
        self.intendedMajor = intededMajor

    # Getters
    def getName(self):
        return self.name
    def getID(self):
        return self.ID
    def getAddress(self):
        return self.address
    def getBirthdate(self):
        return self.birthdate
    def getAcceptanceDate(self):
        return self.acceptanceDate
    def getSemesterStart(self):
        return self.semesterStart
    def getIntededMajor(self):
        return self.intendedMajor

    def getCourseList(self):
        return self.courseList
    def addCourse(self, course):
        self.courseList.addCourse(course)
    def removeCourse(self, courseNumber):
        return self.courseList.removeCourse(courseNumber)

    def getPhoneList(self):
        return self.phoneList
    def addPhone(self, phone):
        return self.phoneList.addPhone(phone)
    def removePhone(self, phoneNumber):
        return self.phoneList.removePhone(phoneNumber)

    def getEmailList(self):
        return self.emailList
    def addEmail(self, email):
        return self.emailList.addEmail(email)
    def removeEmail(self, emailNumber):
        return self.emailList.removeEmail(emailNumber)

    def displayCourses(self):
        current = self.courseList.head
        count = 1
        if current is None:
            print("No courses enrolled yet.")
        else:
            while current:
                print(f"{count}. {current.getCourse()}")  # <<== Use .getCourse() because __course is private
                current = current.next
                count += 1

    def __str__(self):
        return (f"Student Name: {self.name}\n"
                f"Student ID: {self.ID}\n"
                f"Student Address: {self.address}\n"
                f"Student Emails: \n{self.emailList}\n"
                f"Student Phone Numbers: \n{self.phoneList}\n"
                f"Student Birthdate: {self.birthdate}\n"
                f"Student Acceptance Date: {self.acceptanceDate}\n"
                f"Student Semester Start Date: {self.semesterStart}\n"
                f"Student Intended Major: {self.intendedMajor}\n"
                f"Student Courses: \n{self.courseList}")
