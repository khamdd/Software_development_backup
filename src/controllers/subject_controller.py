from src.models.student import Student
from src.models.database import Database
from src.models.subject import Subject
from src.common.utils import Utils

class SubjectController:
    def __init__(self, current_student, database: Database):
        self.database = database
        self.current_student: Student = self.get_current_student_database(current_student)
        self.show_menu()
        
    def list_subjects(self):
        print(f"Showing {self.current_student.subjects.__len__()} subjects")
        for subject in self.current_student.subjects:
            print(subject)
            
    def enroll_subject(self):
        if(self.current_student.subjects.__len__() == 4):
            print("Students are allowed to enrol in 4 subjects only")
            return
        new_subject = Utils().get_random_subject(self.current_student.subjects)
        self.current_student.subjects.append(new_subject)
        
        self.database.write_file()
        print(f"Enrolling in Subject-{new_subject.subject_id}")
        print(f"You are now enrolled in {self.current_student.subjects.__len__()} out of 4 subjects")
        
    def change_password(self):
        print("Updating Password")
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        if(Utils().check_password(new_password) and (new_password == confirm_password)):
            self.current_student.password = new_password
            self.database.write_file()
            print("Password changed successfully")
        elif(new_password != confirm_password):
            print("Password does not match - try again")
        else:
            print("Incorrect password format")
            
    def remove_subject(self):
        if(self.current_student.subjects.__len__() == 0):
            print("No subjects to remove")
            return
        
        print(f"Remove Subject by ID: {self.current_student.subjects[-1].subject_id}")
        print(f"Dropping Subject-{self.current_student.subjects[-1].subject_id}")
        self.current_student.subjects.pop()
        
        print(f"You are now enrolled in {self.current_student.subjects.__len__()} out of 4 subjects")
        self.database.write_file()

    def get_current_student_database(self, current_student) -> Student:
        if(self.database.student_list.__len__() == 0):
            return None
        for student in self.database.student_list:
            if student.student_id == current_student.student_id:
                return student

    def show_menu(self):
        choice = ""
        while(choice != "x"):
            choice = input("Student Course Menu (c/e/r/s/x): ")
            
            if(choice == "c"): self.change_password()
            elif(choice == "e"): self.enroll_subject()
            elif(choice == "r"): self.remove_subject()
            elif(choice == "s"): self.list_subjects()
            elif(choice == "x"): pass
            else: print("Invalid choice, please try again")