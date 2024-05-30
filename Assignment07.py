# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# Change Log: (Who, When, What)
#   JP,13MAT24,Created Script
#   JP,16MAY24,Added Exception
#   JP,22MAY24,Added Classes and Functions
#   JP,26MAY24,Class Inheritance
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants and variables
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
#Define the variables
students: list = []  # a table of student data NEEDS TO BE USED
menu_choice: str = '' # Hold the choice made by the user.

# --------SEPARATION OF CONCERNS-------------
#   OBJECT LAYER
#       Class: Person
#
#   DATA LAYER
#       Class: FileProcessor
#
#   PRESENTATION LAYER
#       Class: IO
#
#   PROCESSING LAYER
#       Create/Read JSON file
#       Execute functions
#       Terminate program
# -------------------------------------------

# ---------DATA LAYER-----------------------
# Define the Data Variables


# Processing --------------------------------------- #

# Create a Person Class
class Person:
    '''
        The Person class is a parent class for Student and derivatives thereof.

        ChangeLog: (Who, When, What)
        JP,26MAY24,Created Class
    '''

# Add first_name and last_name properties to the constructor
    def __init__(self, student_first_name: str = '', student_last_name: str = '' ): #<function> <constructor/init method>(<instance_referenced>,<argument,>,<argument>): #private attributes
        self.student_first_name = student_first_name #<instance_referenced>.<attribute> = <argument_data> aka instance_variable or attribute
        self.student_last_name = student_last_name #<instance_referenced.<attribute> = <argument_data> aka instance_variable or attribute

# Create a getter for the first_name property
    @property #Use this decorator for the getter or accessor
    def student_first_name(self): #method
        return self.__student_first_name.title() # formatting code

    @student_first_name.setter #Sets the data in place once retrieved
    def student_first_name(self, value: str):
        if value.isalpha() or value == "": # is character or empty string
            self.student_first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

# Create a getter and setter for the last_name property
    @property # Use this decorator for the getter or accessor
    def student_last_name(self):
        return self.__student_last_name.title() # formatting code

    @student_last_name.setter #Sets the data in place once retrieved
    def student_last_name(self, value: str):
        if value.isalpha() or value == "": # is character or empty string
            self.student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

#Override the __str__() method to return Person data in coma-separated string of data
    def __str__(self):
        return f"{self.student_first_name}, {self.student_last_name}"


# Create a Student class the inherits from the Person class
class Student(Person):
    '''
        A child class to the Person class, the student has a course attribute.

        ChangeLog: (Who, When, What)
        JP,26MAY24,Created Class
    '''

# Call to the Person constructor and pass it the first_name and last_name data
    def __init__(self, student_first_name: str = '', student_last_name: str = '', course_name: str = '' ):
# Add a assignment to the course_name property using the course_name parameter
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name) #<Superceding class> <constructor/init method>(<argument,>,<argument>):
        self.course_name = course_name

# # Add the getter for course_name (Done)
#     @property # Use this decorator for the getter or accessor
#     def course_name(self):
#         return self.__course_name.title() # formatting code
# # Add the setter for course_name (Done)
#     @course_name.setter #Sets the data in place once retrieved
#     def course_name(self, value: str):
#         if value.isalpha() or value == "": # is character or empty string
#             self.student_last_name = value
#         else:
#             raise ValueError("The last name should not contain numbers.")

# Override the __str__() method to return the Student data in coma-separated string of data
def __str__(self):
    return f"{self.student_first_name}, {self.student_last_name}, {self.course_name}"
'''
@LegendofKorra If I am understanding this correctly. The reason why I commented out 108 - 120 is because it would be
redundant. Student(child) has inherited the attributes of Person example super().__init__(student_first_name=student_first_name, student_last_name=student_last_name).
No need to set or get. However I do need to add the course name attribute because that is unique to the student class?
'''

class FileProcessor:
    '''
        A collection of processing layer functions that work with json files.

        ChangeLog: (Who, When, What)
        JP,22MAY24,Created Class
    '''
    @staticmethod
    def write_data_to_file(fileName: str, student_data: list):
        """
            This function writes data from a list  to a json file.

            Notes:
                - Data sent to the student_table parameter will be overwritten.
                ChangeLog: (Who, When, What)
                JP,22MAY24,Created function
                :param fileName: string with the name of the file we are reading
                :param student_table: list of dictionary rows we are adding data to
                :return: list of dictionary rows filled newly added data
        """
        try:
            file = open(fileName, "w")
            json.dump(student_data, file)
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            file.close()
            print("The following data was saved to file!")
            return student_data


    @staticmethod
    def read_data_from_file(fileName:str, student_data:list):
        """
            This function reads data from a json file and then displays the data.

            Notes: This data is read from the student_table
                - Data on the file may
                ChangeLog: (Who, When, What)
                JP,22MAY24,Created function
                :param file_name: string with the name of the file we are reading
                :param student_table: list of dictionary rows we are adding data to
        """
        try:
            file = open(fileName, "r")
            student_data = json.load(file)
            for item in students:
                print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, Course: {item['Course']}")
        except FileNotFoundError as e:
            print("JSON file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            json.dump(student_data, file)
            file.close()
        finally:
            IO.output_student_courses(student_data=students)

    @staticmethod
    def creation_of_json(fileName: str, student_data: list):
        """
            This function creates a dictionary if one does not exist for the Professor utilizing the Python Arts script.

            Notes:
                -None
                :param fileName
                :param student_data
                ChangeLog: (Who, When, What)
                JP,26MAY24,Created function
        """
        try:
            file = open(FILE_NAME, "r")
            student_table = json.load(file)
            for item in students:
                print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, Course: {item['Course']}")
        except FileNotFoundError as e:
            print("JSON file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("Prof. Justin will create a JSON for you..")
            student_row1: dict = {"FirstName": "First Name", "LastName": "Last Name", "Course": "Course"}
            student_table: list = [student_row1]
            file = open("Enrollments.json", "w")
            json.dump(student_table, file)
            file.close()
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("JSON document successfully created")

class IO:
    '''
        A collection of input/output (IO) layer functions that work with json files.

        ChangeLog: (Who, When, What)
        JP,22MAY24,Created Class
    '''
    @staticmethod
    def output_error_message(message: str, error: Exception = None):
        """
            This function displays and error message when an Exception is reached.

            Notes:
                -None
                :param message
                :param error
                ChangeLog: (Who, When, What)
                JP,22MAY24,Created function
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def input_menu_choice():
        """
            This function will allow the user to select options 1 - 4 and will raise an exception
            for any other input.

        Notes:
            - None
            ChangeLog: (Who, When, What)
            JP,22MAY24,Created function
            :return: prompts the user to input accepted an accepted input
        """
        try:
            options = {"1", "2", "3", "4"}
            menu_choice = input("What would you like to do: ")
            if menu_choice not in options:
                raise Exception ("Invalid choice. Please enter a number from 1 through 4.")

        except Exception as e:
                IO.output_error_message(e.__str__())
        finally:
            return menu_choice

    @staticmethod
    def output_menu(menu: str):
        """ This function will display the menu options, the MENU is a global constant.

            Notes:
                - None
                ChangeLog: (Who, When, What)
                JP,22MAY24,Created function
                :param menu: str
        """
        global MENU

        print()
        print(MENU)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_student_data(student_data: list):
        """ This function will allow the user to input their first name, last name and course.
            Secondly this adds the newly input data in the student_table. Finally, a message with
            the new data will display to the user what was just added.

            Notes:
                - There are error exceptions if the user inputs numbers when it expects letters
                ChangeLog: (Who, When, What)
                JP,22MAY24,Created function
                :param student_data
        """
        student_first_name: str = ''
        student_last_name: str = ''
        course_name: str = ''

        try:
            # Check that the input does not include numbers
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "Course": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            return student_data

    @staticmethod
    def output_student_courses(student_data:list):
        """ This function will display the current data from student_table which is in JSON format.

            Notes:
            - None
            ChangeLog: (Who, When, What)
            JP,22MAY24,Created function
            :param student_data
        """
        # print("-" * 50)
        # print("\nCurrent registered students:")
        # print(student_data)
        # print("-" * 50)
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["Course"]}')
        print("-" * 50)

#end of class creations

#creation of json file
FileProcessor.creation_of_json(fileName=FILE_NAME, student_data=students)


# Beginning the main body of the script
while True:
    IO.output_menu(menu=MENU)

    # Present the menu of choices
    menu_choice=IO.input_menu_choice()
    # Present the menu of choices

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        # Process the data to create and display a custom message
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(fileName=FILE_NAME, student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
