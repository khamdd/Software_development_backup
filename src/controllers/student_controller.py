from src.common.utils import Utils
from typing import List
from src.models.student import Student
from src.models.database import Database
from src.controllers.subject_controller import SubjectController
import random

class StudentController:
    def __init__(self, database: Database):
        self.current_student: Student = None
        self.database = database

    def register(self):
        print("Student Sign Up")
        while(True):
            email = input("Email: ")
            password = input("Password: ")
            if(Utils().check_email(email) and Utils().check_password(password)):
                print("Email and password format acceptable")
                
                existed_student = Database().check_existed_student(email)
                if(existed_student):
                    print(f"Student {existed_student.name} already exists")
                    break
                else:
                    name = input("Name: ")
                    
                    # Check unique student ID in student_list
                    while True:
                        id = random.randint(1, 999999)
                        if not any(student.student_id == id for student in self.database.student_list):
                            break
                    new_student = Student(id, name, email, password, [])
                    self.database.add_student(new_student)
                    self.database.write_file()
                    print(f"Enrolling Student {name}")
                    break
            else: print("Incorrect email or password format")
    
    def login(self):
        print("Student Sign In")
        while(True):
            email = input("Email: ")
            password = input("Password: ")
            if(Utils().check_email(email) and Utils().check_password(password)):
                print("Email and password format acceptable")
                current_student = Database().student_login(email, password)
                if(current_student):
                    print("Student Sign In")
                    self.current_student = current_student
                    SubjectController(self.current_student, self.database)
                    break
                else:
                    print("Student does not exist")
                    break
            else: print("Incorrect email or password format")