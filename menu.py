from Student import Student
from nameOfStudent import nameOfStudent
from studentID import studentIDNum
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

            while True:
                try:
                    studentIDNum = int(input("Student ID: "))
                    for w in listOfStudents:
                        if w.ID == studentIDNum:
                            raise ValueError("This Student ID is already taken.")
                    else:
                        studentIDNumber = studentID(studentIDNum)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

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
            print("Here is a list of students name and ID:")
            for i in listOfStudents:
                print(f"{i.name}\n{i.ID}")
            studentIDSelected = int(input("Student ID You Would Like to Edit: "))

            for edited in listOfStudents:
                if edited.ID == studentIDSelected:
                    userInputToChange = input("What would you like to change?\n"
                                              "1.Name\n"
                                              "2.ID\n"
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
                                studentIDNum = int(input("Student ID: "))
                                for w in listOfStudents:
                                    if w.ID == studentIDNum:
                                        raise ValueError("This Student ID is already taken.")
                                else:
                                    edited.ID=studentID(studentIDNum)
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid integer.")

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

                else:
                    print("Student Not Found!")


        if userInput == "3":
            for i in listOfStudents:
                print(f"{i.name}\n{i.ID}\n")
            studentToDelete = int(input("Enter Student ID of Student to Delete: "))

            for student in listOfStudents:
                if student.ID == studentToDelete:
                    listOfStudents.remove(student)
                    print(f"Student {student.name} (ID: {student.ID}) has been deleted.")
                    break
            else:
                print("Student not found!")


        if userInput == ("4"):
            for i in listOfStudents:
                print(f"{i.name}\n{i.ID}\n")
            studentToView = int(input("Enter Student ID of Student to View: "))

            for student in listOfStudents:
                if student.ID == studentToView:
                    print(student)
                    break
            else:
                print("Student not found!")


        if userInput == "5":
            print("You have selected to close the program!")
            running = False

    print("Thank you for using this program.")