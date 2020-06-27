'''
Scenario: You are a Database Administrator for a university and need to create an application to
mange student enrollments and balance

Application should the the following:
    - Ask the user how many new students will be added to the database
    - The user should be prompted to enter the name and year for each student
    - The student should have a 5 digit unique ID, with the first number being their grade level
    - A student can enroll in the following courses:
        History 101
        Math 101
        English 101
        Chemistry 101
    - Each course costs $600 to enroll
    - The student should be able to view their balance and pay the tuition
    - A show method that will display the status of the student, should be able to se
    the student name, ID, courses enrolled, and balance
'''

import string

id = 1000


class Student:
    def __init__(self):
        self.fname = self.firstName()
        self.lname = self.lastName()
        self.year, self.gradeLevel = self.student_year()
        self.studentId = self.generateId()
        self.courses = []
        self.tuition = 0

    # get student first name
    def firstName(self):
        while 1:
            fname = input("Enter the student first name: ")
            if fname.isalpha():
                return fname.lower()
            else:
                print("Invalid input")

    # get student last name
    def lastName(self):
        while 1:
            lname = input("Enter the student last name: ")
            if lname.isalpha():
                return lname.lower()
            else:
                print("Invalid input")

    # get the student year
    def student_year(self):
        grade_level = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"}
        while 1:
            try:
                year = int(input("Enter the grade level:\n1 - Freshman\n2 - Sophomore\n3 - Junior\n4 - Senior\n"))
                for k, v in grade_level.items():
                    if year == k:
                        return k, v
            except Exception:
                print("Invalid input try again")

    # get student full name
    @property
    def fullName(self):
        return self.fname + " " + self.lname

    # generate student id
    def generateId(self):
        global id
        id += 1
        studentId = str(self.year) + str(id)
        return studentId

    # Add courses
    def enroll(self):
        while 1:
            print("Press Q|q when done adding")
            course = Course()
            if course.name == "q" or course.name == 'Q':
                break
            self.courses.append(course)
            self.tuition = self.tuition_cal()
            print("\n")

    # show method
    def show(self):
        print(f'\nStudent name: {self.fullName}\nStudent Grade Level: {self.gradeLevel}\nStudent ID: {self.studentId}')
        self.show_courses()
        print(f"Tuition {self.tuition}")

    # Show all the courses the student is taking
    def show_courses(self):
        for course in self.courses:
            print("\t\t" + course.show())

    # Calculate the tuition of the student
    def tuition_cal(self):
        tuition = 0
        for course in self.courses:
            tuition += course.price
        return tuition

    # View balance
    def view_balance(self):
        print(f"\nYour balance is: {self.tuition}")

    # Pay tuition
    def pay_tuition(self):
        while 1:
            try:
                self.view_balance()
                amount = int(input("Enter the amount you want to pay: "))
                if amount >= self.tuition:
                    amount -= self.tuition
                    break
                elif amount < self.tuition and (not amount <= 0):
                    self.tuition -= amount
                    break
                else:
                    print("Invalid amount, try again")
            except Exception:
                print("Invalid input")
        print("Thank you for your payment\n")

# Course Class
class Course:

    def __init__(self):
        self.name = self.course_name()
        self.course_price = 600

    # Get course name
    def course_name(self):
        courseName = input("Enter the name of the course: ")
        return courseName

    # get course price
    @property
    def price(self):
        return self.course_price

    def show(self):
        return f"Course Enrolled: {self.name}, Price: {self.price}"

    @price.setter
    def price(self, value):
        self.price = value

    # get the number of student to add to the database
# Get number of student to add to database
def num_student():
    while 1:
        try:
            num = int(input("\nHow many student do you want to add: "))
            if num > 0:
                return num
            else:
                print("Invalid input")
        except Exception:
            print("Invalid input")
# Show method for the database
def show_database(database):
    for student in database:
        student.show()
# Prompt for user to interact with the app
def prompt():
    choice = int(input(
"""
\nChoose one of the following option:
1- Enroll into a course
2 - View tuition
3 - Pay tuition
4 - Student summary
5 - To quit\n"""))
    return choice
if __name__ == "__main__":
    database = []
    print("\nStudent Database Application\n")
    students = num_student()
    for i in range(0, students):
        student = Student()
        database.append(student)
        while 1:
            choice = prompt()
            if choice == 1:
                database[i].enroll()
            elif choice == 2:
                database[i].view_balance()
            elif choice == 3:
                database[i].pay_tuition()
            elif choice == 4:
                database[i].show()
            elif choice == 5:
                break
            else:
                print("Invalid input")
