# CMPSC132
# Brandon and Gabe
# 3/5/2025

from Student import Student

from nameOfStudent import nameOfStudent
from studentID import studentID
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor

class main():
    listOfStudents = []

    studentName1 = nameOfStudent("Brandon", "Alexander", "Bula")
    studentID1 = studentID(1234567890)
    studentAddress1 = Address("91", "Rabbit Run Road",  "Parkesburg", "PA",  "19365", "Home")
    studentEmail1 = email("helloworld@gmail.com", "Personal")
    studentPhoneNumber1 = phoneNumber("484-123-0987", "Work")
    studentBirthDate1 = Date("04", "12", "2006")
    studentAcceptedDate1 = Date("06", "12", "2024")
    studentSemesterStart1 = Date("08", "30", "2024")
    studentIntendedMajor1 = intendedMajor("Computer Science")

    studentName2 = nameOfStudent("John", "B", "Doe")
    studentID2 = studentID(9876543210)
    studentAddress2 = Address("123", "Baker Street", "Downingtown", "DE", "19335", "Apartment")
    studentEmail2 = email("tester@hotmail.com", "Work")
    studentPhoneNumber2 = phoneNumber("610-789-1234", "Personal")
    studentBirthDate2 = Date("01", "02", "2000")
    studentAcceptedDate2 = Date("06", "12", "2024")
    studentSemesterStart2 = Date("08", "30", "2024")
    studentIntendedMajor2 = intendedMajor("Computer Science")

    student1 = Student(studentName1, studentID1, studentAddress1, studentEmail1, studentPhoneNumber1, studentBirthDate1, studentAcceptedDate1, studentSemesterStart1, studentIntendedMajor1)
    student2 = Student(studentName2, studentID2, studentAddress2, studentEmail2, studentPhoneNumber2, studentBirthDate2, studentAcceptedDate2, studentSemesterStart2, studentIntendedMajor2)

    listOfStudents.append(student1)
    listOfStudents.append(student2)
    for i in listOfStudents:
        print(i.ID)
        firstName = input("First Name: ")
        middleName = input("Middle Name: ")
        lastName = input("Last Name: ")
        studentName = nameOfStudent(firstName, middleName, lastName)
        i.name = studentName
        print(i)

    for i in listOfStudents:
        if i.ID == studentID1:
            pass


class TestStudent():
    main()