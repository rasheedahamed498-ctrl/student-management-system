while True:
    print("\n--- student management system ---")
    print("1, add student")
    print("2, view students")
    print("3, search student")
    print("4, delete student")
    print("5, exit")

    choice = input("enter your choice: ")

   
    if choice == "1":
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()

        with open("students.txt", "a") as file:
            file.write(student_id + " - " + name + "\n")

        print("Student added successfully!")

   
    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                students = file.readlines()

            if len(students) == 0:
                print("No students found.")
            else:
                print("Student list:")
                for student in students:
                    print(student.strip())

        except FileNotFoundError:
            print("No students found.")

    
    elif choice == "3":
        search = input("Enter student ID or name: ").lower().strip()
        found = False

        try:
            with open("students.txt", "r") as file:
                students = file.readlines()

            for student in students:
                if search in student.lower():
                    print("Student found:")
                    print(student.strip())
                    found = True

            if not found:
                print("Student not found.")

        except FileNotFoundError:
            print("No students found.")

    
    elif choice == "4":
        delete_id = input("Enter student ID to delete: ").strip()
        found = False

        try:
            with open("students.txt", "r") as file:
                students = file.readlines()

            updated_students = []

            for student in students:
                if student.strip().startswith(delete_id + " -"):
                    found = True
                else:
                    updated_students.append(student)

            with open("students.txt", "w") as file:
                file.writelines(updated_students)

            if found:
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No students found.")

    
    elif choice == "5":
        print("Exiting program...")
        break

    # INVALID INPUT
    else:
        print("Invalid choice. Try again...")