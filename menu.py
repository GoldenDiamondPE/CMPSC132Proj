# CMPSC132
# Brandon and Gabe
# 3/5/2025
#

from Student import Student
from nameOfStudent import nameOfStudent
from studentIDNum import studentIDNum
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor

def menu(listOfStudents):
    running = True
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

            while True:
                try:
                    studentID = input("\nStudent ID: ")
                    for w in listOfStudents:
                        if w.ID == studentID:
                            raise ValueError("This Student ID is already taken.")
                    else:
                        studentIDNumber = studentIDNum(studentID)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            streetNumber = input("\nStreet Number: ")
            street = input("Street: ")
            city = input("City: ")
            state = input("State: ")
            zipCode = input("Zip Code: ")
            typeOfHouse = input("Type of House: ")
            studentAddress = Address(streetNumber, street, city, state, zipCode, typeOfHouse)

            emailAddress = input("\nEmail: ")
            emailType = input("Email Type: ")
            studentEmail = email(emailAddress, emailType)

            number = input("\nPhone Number: ")
            numberType = input("Phone Type: ")
            studentPhoneNumber = phoneNumber(number, numberType)

            monthBorn = input("\nMonth Born: ")
            dayBorn = input("Day Born: ")
            yearBorn = input("Year Born: ")
            birthday = Date(monthBorn, dayBorn, yearBorn)

            monthAccepted = input("\nMonth Accepted: ")
            dayAccepted = input("Day Accepted: ")
            yearAccepted = input("Year Accepted: ")
            acceptanceDate = Date(monthAccepted, dayAccepted, yearAccepted)

            monthSemesterStart = input("\nMonth Semester Start: ")
            daySemesterStart = input("Day Semester Start: ")
            yearSemesterStart = input("Year Semester Start: ")
            semesterStart = Date(monthSemesterStart, daySemesterStart, yearSemesterStart)

            intendedMajorPicked = input("\nIntended Major: ")
            StudentIntendedMajor = intendedMajor(intendedMajorPicked)

            studentInfo = Student(studentName, studentIDNumber, studentAddress, studentEmail, studentPhoneNumber, birthday, acceptanceDate, semesterStart, StudentIntendedMajor)

            listOfStudents.append(studentInfo)

            print(f"You Finished Creating {studentName}")


        if userInput == "2":
            print("Here is a list of students name and ID:")
            for i in listOfStudents:
                print(f"{i.name}\n{i.ID}\n")
            studentIDSelected = input("Student ID You Would Like to Edit: ")

            for edited in listOfStudents:
                if edited.ID.getStudentID() == studentIDSelected:
                    userInputToChange = input("What would you like to change?\n"
                                              "1. Name\n"
                                              "2. ID\n"
                                              "3. Address\n"
                                              "4. Email\n"
                                              "5. Phone Number\n"
                                              "6. Birthdate\n"
                                              "7. Acceptance Date\n"
                                              "8. Semester Start\n"
                                              "9. Intended Major\n")

                    if userInputToChange == "1":
                        firstName = input("First Name: ")
                        middleName = input("Middle Name: ")
                        lastName = input("Last Name: ")
                        edited.name = nameOfStudent(firstName, middleName, lastName)

                    elif userInputToChange == "2":
                        while True:
                            try:
                                studentID = input("Student ID: ")
                                for possibleStudent in listOfStudents:
                                    if possibleStudent.ID.getStudentID() == studentID:
                                        print("This Student ID is already taken.")
                                        raise ValueError()
                                else:
                                    edited.ID=studentIDNum(studentID)
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid ID.")

                    elif userInputToChange == "3":
                        streetNumber = input("Street Number: ")
                        street = input("Street: ")
                        city = input("City: ")
                        state = input("State: ")
                        zipCode = input("Zip Code: ")
                        typeOfHouse = input("Type of House: ")
                        edited.address = Address(streetNumber, city, state, zipCode, typeOfHouse)

                    elif userInputToChange == "4":
                        emailAddress = input("Email: ")
                        emailType = input("Email Type: ")
                        edited.email = email(emailAddress, emailType)

                    elif userInputToChange == "5":
                        number = input("Phone Number: ")
                        numberType = input("Phone Type: ")
                        edited.phone = phoneNumber(number, numberType)

                    elif userInputToChange == "6":
                        month = input("Month: ")
                        day = input("Day: ")
                        year = input("Year: ")
                        edited.birthdate = Date(month, day, year)

                    elif userInputToChange == "7":
                        month = input("Month: ")
                        day = input("Day: ")
                        year = input("Year: ")
                        edited.acceptanceDate = Date(month, day, year)

                    elif userInputToChange == "8":
                        month = input("Month: ")
                        day = input("Day: ")
                        year = input("Year: ")
                        edited.semesterStart = Date(month, day, year)

                    elif userInputToChange == "9":
                        intendedMajorPicked = input("Intended Major: ")
                        edited.intendedMajor = intendedMajor(intendedMajorPicked)



        if userInput == "3":
            for i in listOfStudents:
                print(f"{i.name}\n{i.ID}\n")
            studentToDelete = input("Enter Student ID of Student to Delete: ")

            for student in listOfStudents:
                if student.ID.getStudentID() == studentToDelete:
                    print(f"Student {student.name} (ID: {student.ID}) has been deleted.")
                    listOfStudents.remove(student)
                    break


        if userInput == "4":
            for i in listOfStudents:
                print(f"{i.name}\n{i.ID}\n")
            studentToView = input("Enter Student ID of Student to View: ")

            for student in listOfStudents:
                if student.ID.getStudentID() == studentToView:
                    print(student)
                    break
            else:
                print("Student not found!")


        if userInput == "5":
            print("You have selected to close the program!")
            running = False

    print("Thank you for using this program.")