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
    studentName1 = nameOfStudent("Brandon", "Alexander", "Bula")
    studentID1 = studentID(1234567890)
    studentAddress = Address("91", "Rabbit Run Road",  "Parkesburg", "PA",  "19365", "Home")
    studentEmail = email("helloworld@gmail.com", "Personal")
    studentPhoneNumber = phoneNumber("484-123-0987", "Work")
    studentBirthDate = Date("04", "12", "2006")
    studentAcceptedDate = Date("06", "12", "2024")
    studentSemesterStart = Date("08", "30", "2024")
    studentIntendedMajor = intendedMajor("Computer Science")

    student1 = Student(studentName1, studentID1, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)

    print(student1)

class TestStudent():
    main()