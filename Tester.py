# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# CMPSC 132
# 3/24/2025
# This program uses 5 example students to demonstrate the functionality of the Academic Advisor Program
from Advisor import Advisor
from Student import Student
from nameOfStudent import nameOfStudent
from studentIDNum import studentIDNum
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor
from StudentMenu import menu

from AdvisorMenu import AdvisorMenu
from Course import Course
from CourseLinkedList import CourseLinkedList
from EmailLinkedList import EmailLinkedList
from PhoneLinkedList import PhoneLinkedList

listOfStudents = []
listOfAdvisors = []


# Fills out example of student info
studentName = nameOfStudent("Brandon", "Alexander", "Bula")
studentID = studentIDNum("1234567890")
studentAddress = Address("91", "Rabbit Run Road",  "Parkesburg", "PA",  "19365", "Home")
studentBirthDate = Date("04", "12", "2006")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")
Course4 = Course("CHEM110", "Fall 2022", "Hybrid", "Completed", "B")
Course5 = Course("HIST020", "Spring 2023", "In-person", "Dropped", "N/A")
Course6 = Course("ENGL015", "Fall 2023", "Remote", "On-going", "N/A")

# Appends student info
student1 = Student(studentName, studentID, studentAddress, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student1.addPhone(phoneNumber("484-123-0987", "Work"))
student1.addEmail(email("helloworld@gmail.com", "Personal"))
student1.addCourse(Course4)
student1.addCourse(Course5)
student1.addCourse(Course6)
listOfStudents.append(student1)

studentName = nameOfStudent("John", "B", "Doe")
studentID = studentIDNum("7203650189")
studentAddress = Address("123", "Baker Street", "Downingtown", "DE", "19335", "Apartment")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")
Course7 = Course("ECON102", "Spring 2022", "In-person", "Completed", "A")
Course8 = Course("BIOL141", "Fall 2023", "Hybrid", "On-going", "N/A")
Course9 = Course("PSYCH100", "Summer 2023", "Remote", "Completed", "C")

student2 = Student(studentName, studentID, studentAddress, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student2.addEmail(email("tester@hotmail.com", "Work"))
student2.addPhone(phoneNumber("610-789-1234", "Personal"))
student2.addCourse(Course7)
student2.addCourse(Course8)
student2.addCourse(Course9)
listOfStudents.append(student2)

studentName = nameOfStudent("Mac", "C", "Conor")
studentID = studentIDNum("1")
studentAddress = Address("986", "Summer Lane", "Fore", "CA", "18753", "House")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Biology")
Course1 = Course("CMPSC122", "Spring 2023", "In-person", "Completed", "A")
Course2 = Course("MATH140", "Fall 2023", "Remote", "Completed", "B")
Course3 = Course("PHYS211", "Spring 2024", "Hybrid", "On-going", "N/A")

student3 = Student(studentName, studentID, studentAddress, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student3.addCourse(Course1)
student3.addCourse(Course2)
student3.addCourse(Course3)
student3.addPhone(phoneNumber("123-456-7891", "Personal"))
student3.addEmail(email("tester@yahoo.com", "Work"))
listOfStudents.append(student3)

studentName = nameOfStudent("Charles", "Q", "Pop")
studentID = studentIDNum("6329103729")
studentAddress = Address("524", "Runner Street", "Broke", "DE", "19335", "Apartment")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Political Science")
Course10 = Course("ART101", "Fall 2021", "In-person", "Completed", "B")
Course11 = Course("PHIL103", "Spring 2022", "Remote", "Dropped", "N/A")
Course12 = Course("SPAN100", "Spring 2024", "Hybrid", "On-going", "N/A")

student4 = Student(studentName, studentID, studentAddress, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student4.addPhone(phoneNumber("867-193-7489", "Personal"))
student4.addEmail(email("bingbong@gmail.com", "Work"))
student4.addCourse(Course10)
student4.addCourse(Course11)
student4.addCourse(Course12)
listOfStudents.append(student4)

studentName = nameOfStudent("Dom", "B", "Sinclear")
studentID = studentIDNum("2470836766")
studentAddress = Address("757", "Rabbit Run Road", "Getty", "DE", "83024", "Apartment")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")
Course13 = Course("STAT200", "Fall 2022", "In-person", "Completed", "A")
Course14 = Course("ANTH045", "Summer 2022", "Remote", "Completed", "B")
Course15 = Course("MUSIC005", "Spring 2023", "Hybrid", "On-going", "N/A")

student5 = Student(studentName, studentID, studentAddress, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student5.addPhone(phoneNumber("610-789-1234", "Personal"))
student5.addEmail(email("tester@hotmail.com", "Work"))
student5.addEmail(email("woker@gmail.com","Personal"))
student5.addCourse(Course13)
student5.addCourse(Course14)
student5.addCourse(Course15)
listOfStudents.append(student5)


# Advisors
advisor1 = Advisor("John", "Bigfoot", "A", "Professor", "Computer Science")
advisor1.addAdvisee(student1.getID())
advisor1.addAdvisee(student2.getID())
advisor1.addAdvisee(student3.getID())
listOfAdvisors.append(advisor1)

advisor2 = Advisor("Chris", "Cracker", "B", "Instructor", "English")
advisor2.addAdvisee(student4.getID())
listOfAdvisors.append(advisor2)

advisor3 = Advisor("Samantha", "Jones", "C", "Adjunct", "Biology")
advisor3.addAdvisee(student5.getID())
listOfAdvisors.append(advisor3)


if __name__ == "__main__":
    while True:
        user = int(input("Which Subject Would You Like to Modify:\n"
                         "1. Student\n"
                         "2. Advisor\n"
                         "3. Quit\n"))
        if user == 1:
            menu(listOfStudents)
        elif user == 2:
            AdvisorMenu(listOfAdvisors,listOfStudents)
        elif user == 3:
            break
    print("\nThank You For Using Our Program!")
