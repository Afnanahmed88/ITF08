import random

name = input("Enter your name: ")
delivery_date = input("Enter submission date: ")

print("Name: ", name)
print("Delivery Date: ", delivery_date)

class Course:
    def init(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark

    def display_course_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Mark: {self.course_mark}")

class Student:
    total_students = 0

    def init(self, student_name, student_age, student_number):
        self.student_id = random.randint(1000, 9999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

        Student.total_students += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    def get_student_details(self):
        return {
            "Student ID": self.student_id,
            "Student Name": self.student_name,
            "Student Age": self.student_age,
            "Student Number": self.student_number
        }

    def get_student_courses(self):
        print("Student Courses:")
        for course in self.courses_list:
            course.display_course_info()

    def get_student_average(self):
        if not self.courses_list:
            return 0
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)


students_dict = {}

def add_student():
    student_number = input("Enter Student Number: ")
    student_name = input("Enter Student Name: ")
    student_age = int(input("Enter Student Age: "))

    student = Student(student_name, student_age, student_number)
    students_dict[student_number] = student

    print("Student Added Successfully")

def delete_student():
    student_number = input("Enter Student Number: ")
    if student_number in students_dict:
        del students_dict[student_number]
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")

def display_student():
    student_number = input("Enter Student Number: ")
    if student_number in students_dict:
        student = students_dict[student_number]
        student_details = student.get_student_details()
        print("\nStudent Details:")
        for key, value in student_details.items():
            print(f"{key}: {value}")
        student.get_student_courses()
    else:
        print("Student Not Found")

def get_student_average():
    student_number = input("Enter Student Number: ")
    if student_number in students_dict:
        student = students_dict[student_number]
        average = student.get_student_average()
        if average > 0:
            print(f"\nStudent Average Mark: {average:.2f}")
    else:
        print("Student Not Found")

def add_course():
    student_number = input("Enter Student Number: ")
    if student_number in students_dict:
        student = students_dict[student_number]
        course_name = input("Enter Course Name: ")
        course_mark = float(input("Enter Course Mark: "))
        student.enroll_course(course_name, course_mark)
        print("Course Added to Student Successfully")
    else:
        print("Student Not Found")

while True:
    print("\nStudent Management System")
    print("1. Add New Student")
    print("2. Delete Student")
    print("3. Display Student Details")
    print("4. Get Student Average Mark")
    print("5. Add Course to Student")
    print("6. Exit")

    try:
        selection = int(input("Enter your choice: "))

        if selection == 1:
            add_student()
        elif selection == 2:
            delete_student()
        elif selection == 3:
            display_student()
        elif selection == 4:
            get_student_average()
        elif selection == 5:
            add_course()
        elif selection == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")
    except ValueError:
        print("Invalid input. Please enter a valid number for your selection.")
