from src.models.student import Student
from src.models.database import Database
from typing import Dict, List
from src.common.utils import Utils

class AdminController:
    def __init__(self, database: Database):
        self.database = database
        
    def clear_database(self):
        print("Clearing students database")
        confirm = input("Are you sure you want to clear the database (Y)ES/(N)O: ").lower()
        if(confirm == "y"):
            self.database.student_list = []
            self.database.write_file()
            print("Students data cleared")
        
    def show_all_students(self):
        print("Student List")
        if(not self.database.student_list):
            print("< Nothing to Display >")
            return
        
        for student in self.database.student_list:
            print(f"{student.name} :: {student.student_id} --> Email: {student.email}")
            
    def group_students(self):
        print("Grade Grouping")
        if(not self.database.student_list):
            print("< Nothing to Display >")
            return
        
        
        students_sorted_by_grade = sorted(
            self.database.student_list,
            key=lambda student: sum(subject.mark for subject in student.subjects) / len(student.subjects),
        )
        
        for student in students_sorted_by_grade:
            average_mark = sum(subject.mark for subject in student.subjects) / len(student.subjects)
            print(f"{Utils.grade_calculate(average_mark)} --> {student.name} :: {student.student_id} --> Email: {student.email}")
            
    def remove_student_by_id(self, student_id: int):
        student = self.get_student_by_id(student_id)
        if(student):
            self.database.student_list.remove(student)
            self.database.write_file()
            print(f"Removing Student {student.student_id} Account")
        else:
            print(f"Student {student_id} does not exist")
    
    def get_student_by_id(self, student_id: int) -> Student:
        for student in self.database.student_list:
            if student.student_id == student_id:
                return student
        return None
    
    def partition_students(self):
        print("PASS/FAIL Partition")
        partitioned_students = {
            "FAIL": [],
            "PASS": []
        }
        
        for student in self.database.student_list:
            grade = Utils.grade_calculate(self.get_average_mark(student))
            if(grade != "F"):
                partitioned_students["PASS"].append(student)
            else:
                partitioned_students["FAIL"].append(student)
            
        for key, value in partitioned_students.items():
            students_info = ", ".join(
                f"{student.name} :: {student.student_id} --> GRADE: {self.get_average_mark(student)}"
                for student in value
            )
            print(f"{key} --> [{students_info}]")
                
    def get_average_mark(self, student: Student) -> float:
        return sum(subject.mark for subject in student.subjects) / len(student.subjects)