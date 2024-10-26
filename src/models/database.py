import os
import json
from src.models.student import Student
from typing import List
from src.models.subject import Subject

class Database:
    DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'student.data')
    
    def __init__(self):
        self.path = Database.DATABASE_PATH
        self.check_file_exists()
        self.student_list: List[Student] = self.read_file()
        
    def get_student_list(self) -> List[Student]:
        return self.student_list
    
    def add_student(self, student: Student):
        self.student_list.append(student)
        
    def check_file_exists(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as file:
                print("No database found. Creating new database...")
                json.dump([], file, indent = 4)
    
    def check_existed_student(self, email):
        data = self.read_file()
        
        if(not data):
            return False
        
        for student in data:
            if student.email == email:
                return student
        return False
    
    def student_login(self, email, password):
        data = self.read_file()
        
        if(not data):
            return False
        
        for student in data:
            if student.email == email and student.password == password:
                return student
        return False
        
    def write_file(self):
        with open(self.path, 'w') as file:
            json.dump([student.to_dict() for student in self.student_list], file, indent = 4)
            
    def read_file(self) -> List[Student]:
        with open(self.path, 'r') as file:
            try:
                data = json.load(file)
                modified_data: List[Student] = []
                for student in data:
                    subjects = [Subject(**subject) for subject in student['subjects']]
                    student.pop('subjects')
                    modified_student = Student(**student, subjects=subjects)
                    modified_data.append(modified_student)
                return modified_data
            except json.JSONDecodeError:
                data = []