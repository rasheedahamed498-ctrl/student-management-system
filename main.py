while True:
    print("\n--- student management system ---")
    print("1, add student")
    print("2, view students")
    print("3, exit")

    choice = input("enter your choice: ")

    
    if choice == "1":
        name = input("Enter student name: ")

        with open("students.txt", "a") as file:
            file.write(name + "\n")

        print("Student added successfully!")

    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                students = file.readlines()

            if students == []:
                print("No students found.")
            else:
                print("Student list:")
                for student in students:
                    print(student.strip())

        except FileNotFoundError:
            print("No students found.")

    
    elif choice == "3":
        print("Exiting program...")
        break

    # INVALID INPUT
    else:
        print("Invalid choice. Try again...")