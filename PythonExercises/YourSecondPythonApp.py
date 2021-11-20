"""
Academic System
----------------
- This system should open up to a main menu that allows the user to select from different options:
    1. Class Management
        - Create a new class (new entry in dict)
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

class_info = {}
unenrolled_student_info = {}


# Initial view
def login_prompt():
    print("--------------------------------------------------------->")
    session_off = False
    while not session_off:
        login_user_option = int(input(
            "Welcome to ManageUrSkool! Please select: \n1. Class Management \n2. Student Management \n3. Exit \n"))

        if login_user_option not in [1, 2, 3]:
            print("Please input 1, 2 or 3 to choose between options")
        elif login_user_option == 1:
            print("option 1")
            class_mgmt_prompt()
        elif login_user_option == 2:
            print("option 2")
            student_mgmt_prompt()
        else:
            print("Exiting session")
            session_off = True


# Class management module
def class_mgmt_prompt():
    print("Welcome to Class Management module")
    class_mgmt_session_off = False
    while not class_mgmt_session_off:
        class_mgmt_user_option = int(input(
            "Please select what you'd like to do: \n1. Create new class \n2. Get number of students enrolled in a class \n3. Delete a class \n4. Get the average students grade in the class \n5. Return to home page \n"))

        if class_mgmt_user_option not in [1, 2, 3, 4, 5]:
            print("Please input 1 to 5 to choose between options")
        elif class_mgmt_user_option == 1:
            print("option 1")
            create_new_class(class_info)
        elif class_mgmt_user_option == 2:
            print("option 2")
            get_student_number(class_info)
        elif class_mgmt_user_option == 3:
            print("option 3")
            delete_class(class_info)
        elif class_mgmt_user_option == 4:
            print("option 4")
            class_average_grade(class_info)
        else:
            print("Returning to home page")
            return True


def create_new_class(class_info):
    new_class_key = input("Input the name of the new class \n")
    new_class_temp = {new_class_key: {}}
    class_info.update(new_class_temp)
    print(class_info)
    print("New class " + new_class_key + " created")


def get_student_number(class_info):
    class_to_count = input("Which class are you interested in? \n")
    if class_to_count in class_info:
        print("Number of students enrolled in class " + class_to_count + ": " + str(len(class_info[class_to_count])))
    else:
        print("This class does not exist")


def delete_class(class_info):
    class_to_delete = input("Which class do you want to delete? \n")
    if class_to_delete not in class_info:
        print("This class doesn't exist")
    elif len(class_info[class_to_delete]) < 2:
        class_info.pop(class_to_delete)
        print("Class " + class_to_delete + " successfully deleted")
        print(class_info)
    else:
        print("Can't delete a class comprised of 2 students or more")
        print(class_info)


def class_average_grade(class_info):
    class_grade_input = input("Which class do you want to get average grade from? \n")
    if class_grade_input not in class_info:
        print("This class doesn't exist")
    elif not class_info[class_grade_input]:
        print("No student enrolled in class")
    else:
        class_average = sum([class_info[class_grade_input][x] for x in class_info[class_grade_input]]) / len(
            class_info[class_grade_input])
        print("Average of class " + class_grade_input + " is equal to: " + str(class_average))


# Student management module
def student_mgmt_prompt():
    print("Welcome to Student Management module")
    student_mgmt_session_off = False
    while not student_mgmt_session_off:
        student_mgmt_user_option = int(input(
            "Please select what you'd like to do: \n1. Create a new student account \n2. Delete a student (only if "
            "they are not enrolled in any classes) \n3. Add a grade for a student in a class \n4. Enroll in a class "
            "\n5. Display average grade for each class \n6. Return to home page \n"))

        if student_mgmt_user_option not in [1, 2, 3, 4, 5, 6]:
            print("Please input 1 to 6 to choose between options")
        elif student_mgmt_user_option == 1:
            create_new_student(unenrolled_student_info)
        elif student_mgmt_user_option == 2:
            delete_student(unenrolled_student_info)
        elif student_mgmt_user_option == 3:
            print("option 3")

        elif student_mgmt_user_option == 4:
            print("option 4")

        elif student_mgmt_user_option == 5:
            print("option 5")

        else:
            print("Returning to home page")
            return True

def create_new_student(unenrolled_student_info):
    new_student_key = input("Input the name of the new student \n")
    if new_student_key in unenrolled_student_info:
        print("Student " + new_student_key + " exists already")
    else:
        unenrolled_student_info.update({new_student_key: None})
        print(unenrolled_student_info)
        print("New student " + new_student_key + " account created")

def delete_student(unenrolled_student_info):
    student_to_delete = input("Which student account do you want to delete? \n")
    if student_to_delete in unenrolled_student_info:
        unenrolled_student_info.pop(student_to_delete)
        print("Account of student " + student_to_delete + " successfully deleted")
        print(unenrolled_student_info)
    else:
        print("Student doesn't exist")

login_prompt()
# class_mgmt_prompt()
