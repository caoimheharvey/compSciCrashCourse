"""
Academic System
----------------
- This system should open up to a main menu that allows the user to select from different options:
    1. Class Management
        - Create a new class
        - Get the number of enrolled students in a class
        - Delete a class (only if the number of enrolled students is less than 2)
        - Get the average grade of all students in the class
    2. Student Management
        - Create a new student account
        - Delete a student (only if they are not enrolled in any classes)
        - Add a grade for a student in a class
        - Enroll in a class
        - Display average grade for each class

"""

STUDENTS = {
    'st1': {'name': 'Caoimhe', 'classes': {'cl1': {'grades': [89, 98, 40, 48]}}},
    'st2': {'name': 'Alex', 'classes': {'cl1': {'grades': [58, 34, 43, 92]}, 'cl2': {'grades': [87, 58]}}},
    'st3': {'name': 'Alex', 'classes': {'cl2': {'grades': [65, 85]}}},
}

CLASSES = {
    'cl1': {'class_name': 'Class 1', 'students': ['st1', 'st2']},
    'cl2': {'class_name': 'Class 2', 'students': ['st2', 'st3']}
}


def new_class():
    existing_class_ids = list(CLASSES.keys())
    latest_class_id = "cl00"
    if len(existing_class_ids) > 0:
        latest_class_id = existing_class_ids[-1]
    new_class_id = latest_class_id[:2] + str(int(latest_class_id[2:]) + 1)
    class_name = input("Please enter the class name: ")
    CLASSES[new_class_id] = {'class_name': class_name, 'students': []}
    print(f"Class successfully added with class id: {new_class_id}.")


def num_students_class(class_id):
    if class_id in CLASSES.keys():
        num_students = len(CLASSES[class_id]['students'])
        print(f"Total number of students in {CLASSES[class_id]['class_name']} is {num_students}")
        return num_students


def delete_class():
    class_id = input("Please enter the class ID to remove: ")
    if class_id in CLASSES.keys():
        num_students = num_students_class(class_id)
        if num_students < 2:
            del CLASSES[class_id]
            print("Deleting class...")
        else:
            print("Too many students enrolled, cannot delete.")


def average_class_grade():
    class_id = input("Enter the Class ID you want to get the average grade for: ")
    if class_id in CLASSES.keys():
        total = 0
        for student_id in CLASSES[class_id]['students']:
            total += sum(STUDENTS[student_id]['classes'][class_id]['grades'])
        average = total / len(CLASSES[class_id]['students'])
        print(f"The average class grade is: " + str(average))


def create_student():
    existing_student_ids = list(STUDENTS.keys())
    latest_student_id = "st00"
    if len(existing_student_ids) > 0:
        latest_student_id = existing_student_ids[-1]
    student_id = latest_student_id[:2] + str(int(latest_student_id[2:]) + 1)
    student_name = input("Please enter the student name: ")
    STUDENTS[student_id] = {'student_name': student_name, 'classes': {}}
    print(f"Class successfully added new student with ID: {student_id}.")


def delete_student():
    student_id = input("Please enter the student ID to remove: ")
    if student_id in STUDENTS.keys():
        if len(STUDENTS[student_id]['classes']) == 0:
            del STUDENTS[student_id]
        else:
            print("Unable to remove student")


def add_student_grade():
    student_id = input("Please enter the student ID to receive grade: ")
    class_id = input("Please enter the class ID for the grade: ")
    if student_id in STUDENTS.keys() and class_id in CLASSES.keys():
        grade = float(input("Please enter the grade: "))
        if class_id in STUDENTS[student_id]['classes'].keys():
            STUDENTS[student_id]['classes'][class_id]['grades'].append(grade)
        else:
            print("Student is not enrolled in this class.")


def enroll_student_class():
    student_id = input("Please enter the student ID to be enrolled: ")
    class_id = input("Please enter the class ID for the student enrollment: ")
    if student_id in STUDENTS.keys() and class_id in CLASSES.keys():
        CLASSES[class_id]['students'].append(student_id)
        STUDENTS[student_id]['classes'][class_id] = {'grades': []}
    else:
        print("Could not find student and/or class")


def display_student_grades():
    student_id = input("Please enter the student ID for displaying grades: ")
    if STUDENTS.get(student_id):
        enrolled_classes = STUDENTS[student_id]['classes']
        for class_name, grades in enrolled_classes.items():
            print(class_name, grades)
    else:
        print("Not a valid student")


def student_management():
    print("\nWelcome to the STUDENT management portal")
    return_to_main = False
    options = {
        1: "Create new student account",
        2: "Enroll student in a class",
        3: "Add a students grade",
        4: "Display student grades",
        5: "Delete student account"
    }
    while not return_to_main:
        for k, v in options.items():
            print(f"{k} - {v}")
        selection = int(input("Please enter your selection: "))
        if selection not in options.keys():
            continue
        if selection == 1:
            create_student()
            return_to_main = True
        elif selection == 2:
            enroll_student_class()
            return_to_main = True
        elif selection == 3:
            add_student_grade()
            return_to_main = True
        elif selection == 4:
            display_student_grades()
            return_to_main = True
        elif selection == 5:
            delete_student()
            return_to_main = True
        else:
            print("Invalid selection")


def class_management():
    print("\nWelcome to the CLASS management portal")
    return_to_main = False
    options = {
        1: "Create new class",
        2: "Get number of enrolled students",
        3: "Average grade of a class",
        4: "Delete a class"
    }
    while not return_to_main:
        for k, v in options.items():
            print(f"{k} - {v}")
        selection = int(input("Please enter your selection: "))
        if selection not in options.keys():
            continue
        if selection == 1:
            new_class()
            return_to_main = True
        elif selection == 2:
            class_id = input("Please enter the class ID: ")
            num_students_class(class_id)
            return_to_main = True
        elif selection == 3:
            average_class_grade()
            return_to_main = True
        elif selection == 4:
            delete_class()
            return_to_main = True
        else:
            print("Invalid selection")


exit = False
while not exit:
    selection = input("\nPlease select an option:\n1. Class Management\n2. Student Management\n3. Quit\n")
    if selection == "1":
        class_management()
    elif selection == "2":
        student_management()
    elif selection == "3":
        break
    else:
        print("Invalid option selected...try again")
