import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.controllers.admin_controller import AdminController
from src.controllers.student_controller import StudentController
from src.models.database import Database

class UniversitySystem:
    def __init__(self):
        self.database = Database()
    
    def universitySystem(self):
        choice = ""
        while(choice != "x"):
            choice = input("University System: (A)dmin, (S)tudent, or X: ").lower()
            if(choice == "a"): self.adminSystem()
            elif(choice == "s"): self.studentSystem()
            elif(choice == "x"):
                print("Thank You")
            else:
                print("Invalid choice, please try again")

    def adminSystem(self):
        choice = ""
        admin_controller = AdminController(self.database)
        while(choice != "x"):
            choice = input("Admin System (c/g/p/r/s/x): ").lower()
            if(choice == "c"): admin_controller.clear_database()
            elif(choice == "g"): admin_controller.group_students()
            elif(choice == "p"): admin_controller.partition_students()
            elif(choice == "r"): 
                try:
                    student_id = int(input("Remove by ID: "))
                    admin_controller.remove_student_by_id(student_id)
                except ValueError:
                    print("Invalid student ID")
            elif(choice == "s"): admin_controller.show_all_students()
            elif(choice == "x"): pass
            else:
                print("Invalid choice, please try again")
                
    def studentSystem(self):
        choice = ""
        student_controller = StudentController(self.database)
        
        while(choice != "x"):
            choice = input("Student System (l/r/x): ").lower()
            
            if(choice == "l"): student_controller.login()
            elif(choice == "r"): student_controller.register()
            else:
                print("Invalid choice, please try again")

if __name__ == "__main__":
    uni = UniversitySystem()
    uni.universitySystem()