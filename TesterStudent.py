# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# CMPSC 132
# 3/24/2025
# This program uses 5 example students to demonstrate the functionality of the Academic Advisor Program

from Student import Student
from nameOfStudent import nameOfStudent
from studentIDNum import studentIDNum
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor
from menu import menu

listOfStudents = []

# Fills out example of student info
studentName = nameOfStudent("Brandon", "Alexander", "Bula")
studentID = studentIDNum("1234567890")
studentAddress = Address("91", "Rabbit Run Road",  "Parkesburg", "PA",  "19365", "Home")
studentEmail = email("helloworld@gmail.com", "Personal")
studentPhoneNumber = phoneNumber("484-123-0987", "Work")
studentBirthDate = Date("04", "12", "2006")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")

# Appends student info
student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
listOfStudents.append(student)

studentName = nameOfStudent("John", "B", "Doe")
studentID = studentIDNum("7203650189")
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
studentID = studentIDNum("8759350958")
studentAddress = Address("986", "Summer Lane", "Fore", "CA", "18753", "House")
studentEmail = email("tester@yahoo.com", "Work")
studentPhoneNumber = phoneNumber("123-456-7891", "Personal")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Biology")

student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
listOfStudents.append(student)

studentName = nameOfStudent("Charles", "Q", "Pop")
studentID = studentIDNum("6329103729")
studentAddress = Address("524", "Runner Street", "Broke", "DE", "19335", "Apartment")
studentEmail = email("bingbong@gmail.com", "Work")
studentPhoneNumber = phoneNumber("867-193-7489", "Personal")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Political Science")

student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
listOfStudents.append(student)

studentName = nameOfStudent("Dom", "B", "Sinclear")
studentID = studentIDNum("2470836766")
studentAddress = Address("757", "Rabbit Run Road", "Getty", "DE", "83024", "Apartment")
studentEmail = email("tester@hotmail.com", "Work")
studentPhoneNumber = phoneNumber("610-789-1234", "Personal")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")

student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
listOfStudents.append(student)


if __name__ == "__main__":
    menu(listOfStudents)

# Test code through each meu option
"""
Welocome to out Academic Advisor Managment program to be 
able to quickly edit students information!
What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
4
Brandon Alexander Bula
1234567890

John B Doe
7203650189

Mac C Conor
8759350958

Charles Q Pop
6329103729

Dom B Sinclear
2470836766

Enter Student ID of Student to View: 1234567890
Student Name: Brandon Alexander Bula
Student ID: 1234567890
Student Address: 91 Rabbit Run Road, Parkesburg, PA, 19365. Home
Student Email: helloworld@gmail.com Personal
Student Phone: 484-123-0987 Work
Student Birthdate: 04-12-2006
Student Acceptance Date: 06-12-2024
Student Semester Start Date: 08-30-2024
Student Intended Major: Computer Science

What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
2
Here is a list of students name and ID:
Brandon Alexander Bula
1234567890

John B Doe
7203650189

Mac C Conor
8759350958

Charles Q Pop
6329103729

Dom B Sinclear
2470836766

Student ID You Would Like to Edit: 1234567890
What would you like to change?
1. Name
2. ID
3. Address
4. Email
5. Phone Number
6. Birthdate
7. Acceptance Date
8. Semester Start
9. Intended Major
2
Student ID: 1234567890
This Student ID is already taken.
Invalid input. Please enter a valid ID.
Student ID: 27304897234782470
What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
4
Brandon Alexander Bula
27304897234782470

John B Doe
7203650189

Mac C Conor
8759350958

Charles Q Pop
6329103729

Dom B Sinclear
2470836766

Enter Student ID of Student to View: 27304897234782470
Student Name: Brandon Alexander Bula
Student ID: 27304897234782470
Student Address: 91 Rabbit Run Road, Parkesburg, PA, 19365. Home
Student Email: helloworld@gmail.com Personal
Student Phone: 484-123-0987 Work
Student Birthdate: 04-12-2006
Student Acceptance Date: 06-12-2024
Student Semester Start Date: 08-30-2024
Student Intended Major: Computer Science

What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
3
Brandon Alexander Bula
27304897234782470

John B Doe
7203650189

Mac C Conor
8759350958

Charles Q Pop
6329103729

Dom B Sinclear
2470836766

Enter Student ID of Student to Delete: 27304897234782470
Student Brandon Alexander Bula (ID: 27304897234782470) has been deleted.
What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
4
John B Doe
7203650189

Mac C Conor
8759350958

Charles Q Pop
6329103729

Dom B Sinclear
2470836766

Enter Student ID of Student to View: 1
Student not found!
What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
1
First Name: Brandon
Middle Name: A
Last Name: Bula

Student ID: 27304897234782470

Street Number: 51
Street: Carmine Street
City: Downingtown
State: PA
Zip Code: 19335
Type of House: Apartment

Email: huwfebwei@hotmail.com
Email Type: Personal

Phone Number: 422-738-8392
Phone Type: Cell

Month Born: 04
Day Born: 12
Year Born: 2006

Month Accepted: 06
Day Accepted: 1
Year Accepted: 2024

Month Semester Start: 08
Day Semester Start: 31
Year Semester Start: 2024

Intended Major: Computer Science
You Finished Creating Brandon A Bula
What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
4
John B Doe
7203650189

Mac C Conor
8759350958

Charles Q Pop
6329103729

Dom B Sinclear
2470836766

Brandon A Bula
27304897234782470

Enter Student ID of Student to View: 27304897234782470
Student Name: Brandon A Bula
Student ID: 27304897234782470
Student Address: 51 Carmine Street, Downingtown, PA, 19335. Apartment
Student Email: huwfebwei@hotmail.com Personal
Student Phone: 422-738-8392 Cell
Student Birthdate: 04-12-2006
Student Acceptance Date: 06-1-2024
Student Semester Start Date: 08-31-2024
Student Intended Major: Computer Science

What would you like to do?
1. Create a Student
2. Edit a Student
3. Delete a Student
4. Display a Student
5. Quit
5
You have selected to close the program!
Thank you for using this program.
"""
