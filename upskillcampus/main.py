from database import connect
from student import *

connect()

while True:

    print("\n" + "=" * 90)
    print("               STUDENT MANAGEMENT SYSTEM")
    print("=" * 90)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        print("\n------ Add Student ------")

        name = input("Name   : ")
        age = int(input("Age    : "))
        course = input("Course : ")
        email = input("Email  : ")
        phone = input("Phone  : ")

        add_student(name, age, course, email, phone)

        print("\nStudent Added Successfully.")

    elif choice == "2":

        students = view_students()

        if not students:
            print("\nNo Students Found.")
        else:

            print("\n" + "-" * 115)
            print("{:<5} {:<25} {:<5} {:<15} {:<35} {:<15}".format(
                "ID", "NAME", "AGE", "COURSE", "EMAIL", "PHONE"
            ))
            print("-" * 115)

            for s in students:
                print("{:<5} {:<25} {:<5} {:<15} {:<35} {:<15}".format(
                    s[0],
                    s[1],
                    s[2],
                    s[3],
                    s[4],
                    s[5]
                ))

            print("-" * 115)

    elif choice == "3":

        sid = int(input("\nEnter Student ID: "))

        student = search_student(sid)

        if student:

            print("\nStudent Details")
            print("-" * 40)
            print(f"ID     : {student[0]}")
            print(f"Name   : {student[1]}")
            print(f"Age    : {student[2]}")
            print(f"Course : {student[3]}")
            print(f"Email  : {student[4]}")
            print(f"Phone  : {student[5]}")
            print("-" * 40)

        else:
            print("\nStudent Not Found.")

    elif choice == "4":

        sid = int(input("\nEnter Student ID: "))

        student = search_student(sid)

        if student:

            print("\nEnter New Details")

            name = input("Name   : ")
            age = int(input("Age    : "))
            course = input("Course : ")
            email = input("Email  : ")
            phone = input("Phone  : ")

            update_student(sid, name, age, course, email, phone)

            print("\nStudent Updated Successfully.")

        else:
            print("\nStudent Not Found.")

    elif choice == "5":

        sid = int(input("\nEnter Student ID: "))

        student = search_student(sid)

        if student:
            delete_student(sid)
            print("\nStudent Deleted Successfully.")
        else:
            print("\nStudent Not Found.")

    elif choice == "6":

        print("\nThank You for Using Student Management System.")
        break

    else:
        print("\nInvalid Choice. Please Try Again.")