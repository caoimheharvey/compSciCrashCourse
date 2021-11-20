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

# key class, value student id
class_info = {'Math': [1, 2, 3],
              'CS': [1, 3],
              'Art': [4]}

# key student id, value dict storing name, class grades
student_info = {1: {'name': 'Alex', 'Math': 80, 'CS': 30}, 2: {'name': 'Caoimhe', 'Math': 50}, 3: {'name': 'Chou', 'CS': 90, 'Math': 80}, 4: {'name': 'Hans', 'Art': 10}}


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
            class_average_grade(class_info, student_info)
        else:
            print("Returning to home page")
            return True


def create_new_class(class_info):
    new_class_key = input("Input the name of the new class \n")
    new_class_temp = {new_class_key: []}
    class_info.update(new_class_temp)
    print(class_info)
    print("New class " + new_class_key + " created")


def get_student_number(class_info):
    class_to_count = input("Which class are you interested in? \n")
    if class_to_count in class_info:
        print("Number of students enrolled in class " + class_to_count + ": " + str(len(class_info[class_to_count])))
    else:
        print("This class does not exist")


# deleting class should delete student grade in class as well
def delete_class(class_info):
    class_to_delete = input("Which class do you want to delete? \n")
    if class_to_delete not in class_info:
        print("This class doesn't exist")
    elif len(class_info[class_to_delete]) < 2:
        for i in class_info[class_to_delete]:
            student_info[i].pop(class_to_delete)
        class_info.pop(class_to_delete)
        print(class_to_delete + " class successfully deleted")
        print(class_info)
        print(student_info)
    else:
        print("Can't delete a class comprised of 2 students or more")
        print(class_info)


def class_average_grade(class_info, student_info):
    class_grade_input = input("Which class do you want to get average grade from? \n")
    if class_grade_input not in class_info:
        print("This class doesn't exist")
    elif not class_info[class_grade_input]:
        print("No student enrolled in class")
    else:
        class_average = sum([student_info[x][class_grade_input] for x in class_info[class_grade_input]]) / len(
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
            create_new_student(student_info)
        elif student_mgmt_user_option == 2:
            delete_student(student_info)
        elif student_mgmt_user_option == 3:
            change_student_grade(class_info)
        elif student_mgmt_user_option == 4:
            enroll_student_to_class(class_info, student_info)
        elif student_mgmt_user_option == 5:
            print("option 5")

        else:
            print("Returning to home page")
            return True


def create_new_student(student_info):
    new_student_name = input("Input the name of the new student \n")
    new_student_key = sorted(student_info.keys())[-1] + 1
    student_info.update({new_student_key: {'name': new_student_name}})
    print(student_info)
    print("New student " + new_student_name + " account created")


def delete_student(student_info):
    print(student_info)
    student_to_delete = input("Please input the ID of the student account you wish to delete \n")
    if int(student_to_delete) in student_info:
        student_info.pop(int(student_to_delete))
        print("Account of student ID " + student_to_delete + " successfully deleted")
        print(student_info)
    else:
        print("ID is incorrect or student doesn't exist")


def change_student_grade(class_info):
    student_grade_prompt = input("Please input the ID of the student account you want to change grade for \n")
    if int(student_grade_prompt) in student_info:
        student_grade_class_prompt = input("For which class are you change grade for? \n")
        if student_grade_class_prompt in student_info[int(student_grade_prompt)]:
            grade_prompt = input("Please input the grade for the selected class \n")
            if grade_prompt.isnumeric() and int(grade_prompt) >= 0 and int(grade_prompt) < 101:
                student_info[int(student_grade_prompt)][student_grade_class_prompt] = grade_prompt
                print("Grade changed successfully")
                print(student_info)
            else:
                print("Grade should be within 0 and 100")
        else:
            print("Class is incorrect or doesn't exist")
    else:
        print("ID is incorrect or student doesn't exist")


def enroll_student_to_class(class_info, student_info):
    print(student_info)
    student_to_enroll_prompt = input("Please input the ID of the student you'd like to enroll \n")
    if int(student_to_enroll_prompt) in student_info:
        class_to_enroll_prompt = input("In which class would you like to enroll the student to? \n")
        if class_to_enroll_prompt in class_info:
            if int(student_to_enroll_prompt) in class_info[class_to_enroll_prompt]:
                print("Student is already enrolled in this class")
            else:
                class_info[class_to_enroll_prompt].append(int(student_to_enroll_prompt))
                student_info[int(student_to_enroll_prompt)].update({class_to_enroll_prompt: None})
                print(class_info)
                print(student_info)
        else:
            print("Class doesn't exist")
    else:
        print("Student doesn't exist or is already enrolled")


login_prompt()
# class_mgmt_prompt()
