from Advisor import Advisor

def AdvisorMenu(studentList):
    advisor = None

    while True:
        choice = input("\nAcademic Advisor Modification\n"
                           "Select an option:\n"
                           "1. Add Advisor\n"
                           "2. Display Advisor Info\n"
                           "3. Edit Advisor Info\n"
                           "4. Exit\n")

        if choice == "1":
            first = input("First Name: ")
            middle = input("Middle Name (or press Enter to skip): ")
            last = input("Last Name: ")
            title = input("Title (Professor, Instructor, Adjunct, etc.): ")
            department = input("Department: ")
            advisor = Advisor(first, last, middle, title, department)
            print(f"Advisor {first} {last} added successfully.")

        elif choice == "2":
            if advisor:
                print("\n--- Advisor Information ---")
                print(advisor)
            else:
                print("No advisor found. Please add one first.")

        elif choice == "3":
            if not advisor:
                print("No advisor found. Please add one first.")
                continue

            while True:
                print("\n--- Edit Advisor ---")
                print("1. Add Advisee")
                print("2. Remove Advisee")
                print("3. Back to Main Menu")
                subChoice = input("Select an option: ")

                if subChoice == "1":
                    # Select from listOfStudents
                    print("\nAvailable Students:")
                    for i, s in enumerate(studentList):
                        print(f"{i + 1}. {s.getName()} (ID: {s.getID()})")

                    idx = int(input("Select student to add (number): ")) - 1
                    if 0 <= idx < len(studentList):
                        advisor.addAdvisee(studentList[idx])
                        print("Student added to advisee list.")
                    else:
                        print("Invalid selection.")

                elif subChoice == "2":
                    sid = input("Enter Student ID to remove: ")
                    if advisor.removeAdvisee(sid):
                        print("Student removed.")
                    else:
                        print("Student not found.")

                elif subChoice == "3":
                    break

                else:
                    print("Invalid input.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid input.")
