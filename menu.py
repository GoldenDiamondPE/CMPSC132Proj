# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/5/2025
# This program prompts the user with options on what to do with a student's info. This includes creating a Student, editing a student, deleting a student, and displaying a Student.

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
    print("Welcome to our Academic Advisor Management program to be \nable to quickly edit students information!")
    while running:
        # Gathers input to decide what option to perform on the student
        userInput = input("What would you like to do?\n"
                          "1. Create a Student\n"
                          "2. Edit a Student\n"
                          "3. Delete a Student\n"
                          "4. Display a Student\n"
                          "5. Quit\n")

        # Creates a student and adds it to the list
        if userInput == "1":
            # Name
            firstName = input("\nFirst Name: ")
            middleName = input("Middle Name: ")
            lastName = input("Last Name: ")
            studentName = nameOfStudent(firstName, middleName, lastName)

            # Student ID
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

            # Address
            streetNumber = input("\nStreet Number: ")
            street = input("Street: ")
            city = input("City: ")
            state = input("State: ")
            zipCode = input("Zip Code: ")
            typeOfHouse = input("Type of House: ")
            studentAddress = Address(streetNumber, street, city, state, zipCode, typeOfHouse)

            # Email
            emailAddress = input("\nEmail: ")
            emailType = input("Email Type: ")
            studentEmails = [email(emailAddress, emailType)]

            # Phone Number
            number = input("\nPhone Number: ")
            numberType = input("Phone Type: ")
            studentPhoneNumber = phoneNumber(number, numberType)

            # Date Born
            monthBorn = input("\nMonth Born: ")
            dayBorn = input("Day Born: ")
            yearBorn = input("Year Born: ")
            birthday = Date(monthBorn, dayBorn, yearBorn)

            # Date Accepted
            monthAccepted = input("\nMonth Accepted: ")
            dayAccepted = input("Day Accepted: ")
            yearAccepted = input("Year Accepted: ")
            acceptanceDate = Date(monthAccepted, dayAccepted, yearAccepted)

            # Semester Start Date
            monthSemesterStart = input("\nMonth Semester Start: ")
            daySemesterStart = input("Day Semester Start: ")
            yearSemesterStart = input("Year Semester Start: ")
            semesterStart = Date(monthSemesterStart, daySemesterStart, yearSemesterStart)

            # Intended Major Picked
            intendedMajorPicked = input("\nIntended Major: ")
            StudentIntendedMajor = intendedMajor(intendedMajorPicked)

            # Combines all info
            studentInfo = Student(studentName, studentIDNumber, studentAddress, studentEmails, studentPhoneNumber, birthday, acceptanceDate, semesterStart, StudentIntendedMajor)

            listOfStudents.append(studentInfo)

            print(f"You Finished Creating {studentName}, {studentIDNumber}!")

        # Edit a Student
        if userInput == "2":
            if len(listOfStudents) == 0:
                print("\nYou have not created any students to edit.\n")
            else:
                editing = True
                while editing:
                    # Determine what student to edit
                    print("\nHere is a list of students name and ID:")
                    for i in listOfStudents:
                        print(f"{i.name}\n{i.ID}\n")
                    studentIDSelected = input("Student ID You Would Like to Edit: ")

                    # Menu to see what gets edited
                    for edited in listOfStudents:
                        if edited.ID.getStudentID() == studentIDSelected:
                            userInputToChange = input("\nWhat would you like to change?\n"
                                                      "1. Name\n"
                                                      "2. ID\n"
                                                      "3. Address\n"
                                                      "4. Email\n"
                                                      "5. Phone Number\n"
                                                      "6. Birthdate\n"
                                                      "7. Acceptance Date\n"
                                                      "8. Semester Start\n"
                                                      "9. Intended Major\n"
                                                      f"10. Quit Editing {edited.getID()}\n")

                            # Name
                            if userInputToChange == "1":
                                firstName = input("First Name: ")
                                middleName = input("Middle Name: ")
                                lastName = input("Last Name: ")
                                edited.name = nameOfStudent(firstName, middleName, lastName)

                            # Student ID
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

                            # Street Number
                            elif userInputToChange == "3":
                                streetNumber = input("Street Number: ")
                                street = input("Street: ")
                                city = input("City: ")
                                state = input("State: ")
                                zipCode = input("Zip Code: ")
                                typeOfHouse = input("Type of House: ")
                                edited.address = Address(streetNumber, city, state, zipCode, typeOfHouse)

                            # Email
                            elif userInputToChange == "4":
                                emailInput = input("What would you like to do with the email?\n"
                                                   "1. Add email\n"
                                                   "2. Change email\n"
                                                   "3. Remove email\n")
                                if emailInput == "1":
                                    emailAddress = input("Email: ")
                                    emailType = input("Email Type: ")
                                    edited.email = email(emailAddress, emailType)
                                    edited.email.append(email(emailAddress, emailType))

                            # Phone Number
                            elif userInputToChange == "5":
                                number = input("Phone Number: ")
                                numberType = input("Phone Type: ")
                                edited.phone = phoneNumber(number, numberType)

                            # Birth Date
                            elif userInputToChange == "6":
                                month = input("Month: ")
                                day = input("Day: ")
                                year = input("Year: ")
                                edited.birthdate = Date(month, day, year)

                            # Acceptance Date
                            elif userInputToChange == "7":
                                month = input("Month: ")
                                day = input("Day: ")
                                year = input("Year: ")
                                edited.acceptanceDate = Date(month, day, year)

                            # Semester Start
                            elif userInputToChange == "8":
                                month = input("Month: ")
                                day = input("Day: ")
                                year = input("Year: ")
                                edited.semesterStart = Date(month, day, year)

                            # Intended Major Picked
                            elif userInputToChange == "9":
                                intendedMajorPicked = input("Intended Major: ")
                                edited.intendedMajor = intendedMajor(intendedMajorPicked)


        # Delete a Student
        if userInput == "3":
            for i in listOfStudents:
                print(f"{i.name}\n{i.ID}\n")
            studentToDelete = input("Enter Student ID of Student to Delete: ")

            for student in listOfStudents:
                if student.ID.getStudentID() == studentToDelete:
                    print(student)
                    confirmDelete = input(f"Delete {student.name} {student.ID.getStudentID()}? (Y/N): ")
                    if confirmDelete == "Y":
                        listOfStudents.remove(student)
                        print(f"Student {student.name} (ID: {student.ID}) has been deleted.")
                    break

        # View a Student
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

        # Quit Program
        if userInput == "5":
            print("You have selected to close the program!")
            running = False

    print("Thank you for using this program.")
