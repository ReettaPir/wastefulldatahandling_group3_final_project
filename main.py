import json
import os
import time

DATA_FILE = "students.json"


def create_data_file_if_missing():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)


def load_students():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def login():
    VALID_USERNAME = "admin"
    VALID_PASSWORD = "password"

    while True:
        given_username = input("Enter username: ")
        given_password = input("Enter password: ")

        if given_username == VALID_USERNAME and given_password == VALID_PASSWORD:
            print("Login successful.")
            break
        else:
            print("Incorrect username or password. Please try again.")


def add_student(students):
    student_number = input("Enter student number: ")
    name = input("Enter student name: ")
    contact = input("Enter student contact information: ")

    for student in students:
        if student["student_number"] == student_number:
            print("Student number already exists.")
            return

    new_student = {
        "student_number": student_number,
        "name": name,
        "contact": contact,
        "grades": []
    }

    students.append(new_student)
    save_students(students)

    print("Student added.")


def add_grade(students):
    student_number = input("Enter student number: ")
    course = input("Enter course name: ")
    grade = input("Enter grade: ")

    student_found = False

    for student in students:
        if student["student_number"] == student_number:
            student["grades"].append({
                "course": course,
                "grade": grade
            })
            student_found = True
            break

    if student_found:
        save_students(students)
        print("Grade added.")
    else:
        print("Student not found.")


def search_student(students):
    student_number = input("Enter student number to search for: ")

    start_time = time.perf_counter()

    found_student = None

    for student in students:
        if student["student_number"] == student_number:
            found_student = student
            break

    end_time = time.perf_counter()

    if found_student:
        print("Student found:")
        print(f"Student Number: {found_student['student_number']}")
        print(f"Name: {found_student['name']}")
        print(f"Contact: {found_student['contact']}")
        print(f"Grades: {found_student['grades']}")
    else:
        print("Student not found.")

    print(f"Search took {end_time - start_time:.6f} seconds.")


def display_all_students(students):
    if not students:
        print("No students found.")
        return

    print("All students:")

    sorted_students = sorted(students, key=lambda s: s["name"])

    for student in sorted_students:
        print(f"Student Number: {student['student_number']}")
        print(f"Name: {student['name']}")
        print(f"Contact: {student['contact']}")
        print(f"Grades: {student['grades']}")
        print()


def count_total_grades(students):
    total = 0
    for student in students:
        for grade in student["grades"]:
            total += 1
    print(f"Total number of grades: {total}")


def display_course_summary(students):

    course_counts = {}

    for student in students:
        for grade in student["grades"]:
            course = grade["course"]

            if course not in course_counts:
                course_counts[course] = 0

            course_counts[course] += 1

    print("Course summary:")

    for course, count in course_counts.items():
        print(f"{course}: {count} grade(s)")

def save_backup(students):
    with open("students_backup.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Backup saved.")


def main():
    create_data_file_if_missing()
    students = load_students()
    login()

    while True:
        print("\nSelect an action:")
        print("1. Add a student")
        print("2. Add grade")
        print("3. Search for student")
        print("4. Display all students")
        print("5. Count total grades")
        print("6. Display course summary")
        print("7. Save backup")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            add_grade(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            display_all_students(students)
        elif choice == "5":
            count_total_grades(students)
        elif choice == "6":
            display_course_summary(students)
        elif choice == "7":
            save_backup(students)
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
