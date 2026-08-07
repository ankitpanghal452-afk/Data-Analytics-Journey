import json
import os


FILE_NAME = "students.json"


class StudentManagementSystem:

    def __init__(self):
        self.students = {}
        self.load_data()

    # -------------------------------
    # Load students from file
    # -------------------------------
    def load_data(self):

        if os.path.exists(FILE_NAME):

            try:
                with open(FILE_NAME, "r") as file:
                    self.students = json.load(file)

            except:
                self.students = {}

        else:
            self.students = {}

    # -------------------------------
    # Save students to file
    # -------------------------------
    def save_data(self):

        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    # -------------------------------
    # Add student
    # -------------------------------
    def add_student(self):

        roll_no = input("Enter roll number: ")

        if roll_no in self.students:
            print("Student already exists.")
            return

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        marks = []

        print("\nEnter marks of 5 subjects:")

        for i in range(5):

            while True:

                try:
                    mark = float(input(f"Subject {i + 1}: "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break

                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        total = sum(marks)
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"

        elif percentage >= 80:
            grade = "A"

        elif percentage >= 70:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        elif percentage >= 50:
            grade = "D"

        else:
            grade = "F"

        self.students[roll_no] = {
            "name": name,
            "age": age,
            "course": course,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        self.save_data()

        print("\nStudent added successfully.")

    # -------------------------------
    # Display all students
    # -------------------------------
    def display_students(self):

        if not self.students:
            print("\nNo students found.")
            return

        print("\n========== ALL STUDENTS ==========")

        for roll_no, student in self.students.items():

            print("\nRoll Number :", roll_no)
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            print("Marks       :", student["marks"])
            print("Total       :", student["total"])
            print("Percentage  :", student["percentage"])
            print("Grade       :", student["grade"])

    # -------------------------------
    # Search student
    # -------------------------------
    def search_student(self):

        roll_no = input("Enter roll number to search: ")

        if roll_no not in self.students:
            print("Student not found.")
            return

        student = self.students[roll_no]

        print("\n========== STUDENT ==========")
        print("Roll Number :", roll_no)
        print("Name        :", student["name"])
        print("Age         :", student["age"])
        print("Course      :", student["course"])
        print("Marks       :", student["marks"])
        print("Total       :", student["total"])
        print("Percentage  :", student["percentage"])
        print("Grade       :", student["grade"])

    # -------------------------------
    # Update student
    # -------------------------------
    def update_student(self):

        roll_no = input("Enter roll number: ")

        if roll_no not in self.students:
            print("Student not found.")
            return

        student = self.students[roll_no]

        print("\nLeave field empty to keep old value.")

        name = input(f"Name ({student['name']}): ")
        age = input(f"Age ({student['age']}): ")
        course = input(f"Course ({student['course']}): ")

        if name:
            student["name"] = name

        if age:
            student["age"] = int(age)

        if course:
            student["course"] = course

        self.save_data()

        print("Student updated successfully.")

    # -------------------------------
    # Delete student
    # -------------------------------
    def delete_student(self):

        roll_no = input("Enter roll number: ")

        if roll_no not in self.students:
            print("Student not found.")
            return

        confirmation = input(
            "Are you sure you want to delete this student? (yes/no): "
        )

        if confirmation.lower() == "yes":

            del self.students[roll_no]

            self.save_data()

            print("Student deleted successfully.")

        else:
            print("Deletion cancelled.")

    # -------------------------------
    # Find topper
    # -------------------------------
    def find_topper(self):

        if not self.students:
            print("No students available.")
            return

        topper_roll = None
        highest_percentage = -1

        for roll_no, student in self.students.items():

            if student["percentage"] > highest_percentage:

                highest_percentage = student["percentage"]
                topper_roll = roll_no

        topper = self.students[topper_roll]

        print("\n========== TOPPER ==========")
        print("Roll Number :", topper_roll)
        print("Name        :", topper["name"])
        print("Percentage  :", topper["percentage"])
        print("Grade       :", topper["grade"])

    # -------------------------------
    # Statistics
    # -------------------------------
    def statistics(self):

        if not self.students:
            print("No students available.")
            return

        total_students = len(self.students)

        passed = 0
        failed = 0

        total_percentage = 0

        for student in self.students.values():

            total_percentage += student["percentage"]

            if student["percentage"] >= 50:
                passed += 1

            else:
                failed += 1

        average = total_percentage / total_students

        print("\n========== STATISTICS ==========")
        print("Total Students :", total_students)
        print("Passed         :", passed)
        print("Failed         :", failed)
        print("Class Average  :", round(average, 2))

    # -------------------------------
    # Main menu
    # -------------------------------
    def menu(self):

        while True:

            print("\n")
            print("================================")
            print("     STUDENT MANAGEMENT SYSTEM")
            print("================================")

            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Find Topper")
            print("7. Statistics")
            print("8. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.find_topper()

            elif choice == "7":
                self.statistics()

            elif choice == "8":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice. Please try again.")


# -----------------------------------
# Program starts here
# -----------------------------------

system = StudentManagementSystem()

system.menu()