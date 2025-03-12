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
from menu import menu

class main():
    listOfStudents = []

    studentName = nameOfStudent("Brandon", "Alexander", "Bula")
    studentID = studentID(1234567890)
    studentAddress = Address("91", "Rabbit Run Road",  "Parkesburg", "PA",  "19365", "Home")
    studentEmail = email("helloworld@gmail.com", "Personal")
    studentPhoneNumber = phoneNumber("484-123-0987", "Work")
    studentBirthDate = Date("04", "12", "2006")
    studentAcceptedDate = Date("06", "12", "2024")
    studentSemesterStart = Date("08", "30", "2024")
    studentIntendedMajor = intendedMajor("Computer Science")

    student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
    listOfStudents.append(student)

    studentName = nameOfStudent("John", "B", "Doe")
    studentID = studentID(9876543210)
    studentAddress = Address("123", "Baker Street", "Downingtown", "DE", "19335", "Apartment")
    studentEmail = email("tester@hotmail.com", "Work")
    studentPhoneNumber = phoneNumber("610-789-1234", "Personal")
    studentBirthDate = Date("01", "02", "2000")
    studentAcceptedDate = Date("06", "12", "2024")
    studentSemesterStart = Date("08", "30", "2024")
    studentIntendedMajor = intendedMajor("Computer Science")

    student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
    listOfStudents.append(student)

    studentName = nameOfStudent("Mac", "C", "Conor")
    studentID = studentID(9876543210)
    studentAddress = Address("986", "Summer Lane", "Fore", "CA", "18753", "House")
    studentEmail = email("tester@yahoo.com", "Work")
    studentPhoneNumber = phoneNumber("123-456-7891", "Personal")
    studentBirthDate = Date("01", "02", "2000")
    studentAcceptedDate = Date("06", "12", "2024")
    studentSemesterStart = Date("08", "30", "2024")
    studentIntendedMajor = intendedMajor("Biology")

    student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
    listOfStudents.append(student)

    studentName = nameOfStudent("John", "B", "Doe")
    studentID = studentID(9876543210)
    studentAddress = Address("123", "Baker Street", "Downingtown", "DE", "19335", "Apartment")
    studentEmail = email("tester@hotmail.com", "Work")
    studentPhoneNumber = phoneNumber("610-789-1234", "Personal")
    studentBirthDate = Date("01", "02", "2000")
    studentAcceptedDate = Date("06", "12", "2024")
    studentSemesterStart = Date("08", "30", "2024")
    studentIntendedMajor = intendedMajor("Computer Science")

    student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
    listOfStudents.append(student)

    studentName = nameOfStudent("John", "B", "Doe")
    studentID = studentID(9876543210)
    studentAddress = Address("123", "Baker Street", "Downingtown", "DE", "19335", "Apartment")
    studentEmail = email("tester@hotmail.com", "Work")
    studentPhoneNumber = phoneNumber("610-789-1234", "Personal")
    studentBirthDate = Date("01", "02", "2000")
    studentAcceptedDate = Date("06", "12", "2024")
    studentSemesterStart = Date("08", "30", "2024")
    studentIntendedMajor = intendedMajor("Computer Science")

    student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
    listOfStudents.append(student)


    for i in listOfStudents:
        print(f"{i.name}\n{i.ID}\n")

    menu()


class TestStudent():
    main()