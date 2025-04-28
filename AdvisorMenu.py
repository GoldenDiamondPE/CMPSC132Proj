from Advisor import Advisor


def AdvisorMenu(advisorList, studentList):
    while True:
        choice = input("\nAcademic Advisor Modification\n"
                           "Select an option:\n"
                           "1. Add Advisor\n"
                           "2. Display Advisor Info\n"
                           "3. Edit Advisor Info\n"
                           "4. Exit\n")

        # Add Advisor
        if choice == "1":
            first = input("First Name: ")
            while not first:
                print("Please enter a first name.")
                first = input("First Name: ")
            middle = input("Middle Name (or press Enter to skip): ")
            last = input("Last Name: ")
            while not last:
                print("Please enter a last name.")
                last = input("Last Name: ")
            title = input("Title (Professor, Instructor, Adjunct, etc.): ")
            department = input("Department: ")
            advisor = Advisor(first, last, middle, title, department)
            advisorList.append(advisor)
            print(f"Advisor {first} {last} added successfully.")

        # Display Advisor Info
        elif choice == "2":
            while True:
                if not advisorList:
                    print("No advisors added.")
                    break
                for i in advisorList:
                    print(f"{i.getFirstName()} {i.getLastName()}\n")

                advisorToViewFirstName = input("Enter advisor's first name: ")
                advisorToViewLastName = input("Enter advisor's last name: ")

                for advisor in advisorList:
                    if advisor.getFirstName() == advisorToViewFirstName and advisor.getLastName() == advisorToViewLastName:
                        print(advisor)

                end = input("\nWould you like to view another advisor? (Y/N)\n")
                if end == "Y":
                    continue
                else:
                    break

        # Edit Advisor Info
        elif choice == "3":
            runner = True
            if not advisorList:
                print("No advisor found. Please add one first.")
                continue

            while runner == True:
                print(f"\nHere are the names of all advisors:")
                for i in advisorList:
                    print(f"{i.getFirstName()} {i.getLastName()}")

                advisorToViewFirstName = input("\nEnter advisor's first name: ")
                advisorToViewLastName = input("Enter advisor's last name: ")

                for advisor in advisorList:
                    if advisor.getFirstName() == advisorToViewFirstName and advisor.getLastName() == advisorToViewLastName:
                        print(f"\nFound Advisor {advisor.getFirstName()} {advisor.getLastName()}.")
                        edits = int(input(f"What would you like to change:\n"
                                            f"1. Name\n"
                                            f"2. Title\n"
                                            f"3. Department\n"
                                            f"4. Advisees\n"
                                            f"5. Quit\n"))
                        # Name
                        if edits == 1:
                            first = input("First Name: ")
                            while not first:
                                print("Please enter a first name.")
                                first = input("First Name: ")
                            middle = input("Middle Name (or press Enter to skip): ")
                            last = input("Last Name: ")
                            while not last:
                                print("Please enter a last name.")
                                last = input("Last Name: ")
                            advisor.setFirstName(first)
                            if middle:
                                advisor.setMiddleName(middle)
                            advisor.setLastName(last)

                        # Title
                        elif edits == 2:
                            title = input("Title (Professor, Instructor, Adjunct, etc.): ")
                            while not title:
                                title = input("Title (Professor, Instructor, Adjunct, etc.): ")
                            advisor.setTitle(title)

                        # Department
                        elif edits == 3:
                            department = input("Department: ")
                            while not department:
                                department = input("Department: ")
                            advisor.setDepartment(department)


                        # Advisees
                        elif edits == 4:
                            subChoice = input(f"\nEdit Advisee Options\n"
                                              f"1. Add Advisee\n"
                                              f"2. Remove Advisee\n"
                                              f"3. View Advisee\n"
                                              f"4. Quit\n")

                            # Add Advisee
                            if subChoice == "1":
                                # Select from listOfStudents
                                print("\nAvailable Students:")
                                for i, students in enumerate(studentList):
                                    print(f"{i + 1}. {students.getName()} (ID: {students.getID()})")

                                studentChoice = int(input(f"Select student to add (Number in List): ")) - 1
                                if 0 <= studentChoice < len(studentList):
                                    advisor.addAdvisee(studentList[studentChoice])
                                    print(f"Student, {studentList[studentChoice].getName()} added to advisee list.")
                                else:
                                    print("Invalid selection.")

                            # Remove Advisee
                            elif subChoice == "2":
                                sid = input("Enter Student ID to remove: ")
                                if advisor.removeAdvisee(sid):
                                    print(f"Student, {sid} removed.")
                                else:
                                    print("Student not found.")

                            # View Advisee
                            elif subChoice == "3":
                                if not advisor.getAdviseeList():
                                    print("No advisees assigned.")
                                else:
                                    print("\nCurrent Advisees:")
                                    print(advisor.getAdviseeList())

                            # Quit
                            elif subChoice == "4":
                                break

                            # Invalid
                            else:
                                print("Invalid input.")

                        # Quit
                        elif edits == 5:
                            print("You Choose to Quit")
                            runner = False

                        # Invalid
                        else:
                            print("Invalid input.")

        # Exit Program
        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid input.")
