"""
A student log
Made by moikkaeel
"""

class Student:

    def __init__(self, name, group, birthday):

        self.name = name
        self.group = group
        self.birthday = birthday

    def __str__(self):
        return f"<{self.name}> \n Class: {self.group} \n Birthday: {self.birthday[0]}/{self.birthday[1]}/{self.birthday[2]}"
    
def add_student(student_log):
    """
    Adds a student to the student log
    """

    print("Submit information.")
    name = input("Name: ")
    group = input("Class: ")
    group = group.upper()

    while True:
        birthday = input("Birthday (DD/MM/YYYY): ")

        birthday = birthday.split("/")

        if len(birthday) < 3:
            print("Incorrect format.")
           
        else:    
            date = int(birthday[0])
            month = int(birthday[1])
            year = int(birthday[2])

            if date > 31:
                print("Incorrect date.")

            elif date == 31 and month in [2, 4, 6, 9, 11]:
                print("Incorrect date.")

            elif date == 29 and month == 2 and year % 4 != 0:
                print("Incorrect date.")

            elif date == 29 and month == 2 and year % 100 == 0 and year % 400 != 0:
                print("Incorrect date.")

            elif month > 12:
                print("Incorrect month.")

            else:
                break

    new_student = Student(name, group, birthday)
    student_log.append(new_student)
    print("Student added.")

def delete_student(student_log):
    """
    Deletes a student from the student log
    """

    name = input("Type in the name of the student: ")

    if len(student_log) == 0:
        print("No students found.")
        return

    for student in student_log:

        if name == student.name:
            student_log.remove(student)
            print(f"Student {name} removed.")
            return

        else:
            print("Student not found.")
            return

def display_students(student_log):
    """
    Displays students
    """

    if len(student_log) == 0:
        print("No students found.")
        return

    print("Students in the student log:")
    for student in student_log:
        print(student)

def search_students(student_log):
    """
    Searches for student in the student log by name
    """

    name = input("Type the name of the student: ")

    if len(student_log) == 0:
        print("No students found.")
        return

    for student in student_log:

        if name == student.name:
            print(student)
            return

        else:
            print("Student not found.")
            return

def main():
    
    student_log = []

    print("Welcome to the student log.")
    print("What do you want to do?")
    print("[A]dd // [D]elete // Dis[P]lay // [S]earch // [Q]uit")

    while True:

        command = input("> ")

        if command == "A" or command == "a":
            print()
            add_student(student_log)
            print()

        elif command == "D" or command == "d":
            print()
            delete_student(student_log)
            print()

        elif command == "P" or command == "p":
            print()
            display_students(student_log)
            print()

        elif command == "S" or command == "s":
            print()
            search_students(student_log)
            print()

        elif command == "Q" or command == "q":
            print()
            print("Thank you for using the student log.")
            return

        else:
            print()
            print("Invalid command!")
            print()

if __name__ == "__main__":
    main()