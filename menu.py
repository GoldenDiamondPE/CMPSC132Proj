from Student import Student
from nameOfStudent import nameOfStudent
from studentID import studentID
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor

class menu():
    running = True
    listOfStudents = []

    while running:
        userInput = input("What would you like to do?\n"
                          "1. Create a Student\n"
                          "2. Edit a Student\n"
                          "3. Delete a Student\n"
                          "4. Display a Student\n"
                          "5. Quit\n")

        if userInput == "1":
            firstName = input("First Name: ")
            middleName = input("Middle Name: ")
            lastName = input("Last Name: ")
            studentName = nameOfStudent(firstName, middleName, lastName)

            studentIDNum = input("Student ID: ")
            studentIDNumber = studentID(studentIDNum)

            streetNumber = input("Street Number: ")
            street = input("Street: ")
            city = input("City: ")
            state = input("State: ")
            zipCode = input("Zip Code: ")
            typeOfHouse = input("Type of House: ")
            studentAddress = Address(streetNumber, street, city, state, zipCode, typeOfHouse)

            emailAddress = input("Email: ")
            emailType = input("Email Type: ")
            studentEmail = email(emailAddress, emailType)

            number = input("Phone Number: ")
            numberType = input("Phone Type: ")
            studentPhoneNumber = phoneNumber(number, numberType)

            monthBorn = input("Month Born: ")
            dayBorn = input("Day Born: ")
            yearBorn = input("Year Born: ")
            birthday = Date(monthBorn, dayBorn, yearBorn)

            monthAccepted = input("Month Accepted: ")
            dayAccepted = input("Day Accepted: ")
            yearAccepted = input("Year Accepted: ")
            acceptanceDate = Date(monthAccepted, dayAccepted, yearAccepted)

            monthSemesterStart = input("Month Semester Start: ")
            daySemesterStart = input("Day Semester Start: ")
            yearSemesterStart = input("Year Semester Start: ")
            semesterStart = Date(monthSemesterStart, daySemesterStart, yearSemesterStart)

            intendedMajorPicked = input("Intended Major: ")
            StudentIntendedMajor = intendedMajor(intendedMajorPicked)

            studentInfo = Student(studentName, studentIDNumber, studentAddress, studentEmail, studentPhoneNumber, birthday, acceptanceDate, semesterStart, StudentIntendedMajor)

            listOfStudents.append(studentInfo)

            print(f"You Finished Creating {studentName}")

        if userInput == "2":
            pass
        # USE STUDENT ID TO SEE

        if userInput == "3":
            for i in listOfStudents:
                print(f"{i}")

            studentToDelete = input("Enter Student ID of Student to Delete: ")

            for i in listOfStudents:
                pass



        if userInput == ("4"):
            for i in listOfStudents:
                print(i)


        if userInput == "5":
            running = False

    print("Thank you for using this program.")