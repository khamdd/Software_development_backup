import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import tkinter as tk
from src.models.student import Student
from src.common.utils import Utils
from tkinter import messagebox as mb
from src.views.exception_window import ExceptionWindow

class EnrolmentWindow:
    def __init__(self, root, current_student, database):
        self.root = root
        self.database = database
        self.current_student = self.get_current_student_database(current_student)
        
        self.enrollment_frame = tk.LabelFrame(self.root, text="Enrolment", padx=20, pady=20, fg="blue", bg="#607b8d")
        self.enrollment_frame.columnconfigure(0, weight=1)
        self.enrollment_frame.columnconfigure(1, weight=1)
        self.enrollment_frame.pack(fill="both", expand="yes", padx=20, pady=20)
        
        enroll_button = tk.Button(self.enrollment_frame, text="Enrol subject", command=self.enrol_subject)
        enroll_button.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        
        show_enrollment_button = tk.Button(self.enrollment_frame, text="Show Enrolment", command=self.show_all_subjects)
        show_enrollment_button.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        
        remove_subject_button = tk.Button(self.enrollment_frame, text="Remove subject", command=self.remove_subject)
        remove_subject_button.grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        
        logout_button = tk.Button(self.enrollment_frame, text="Logout", command=self.show_login)
        logout_button.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        
    def enrol_subject(self):
        if(self.current_student.subjects.__len__() == 4):
            ExceptionWindow("Students are allowed to enrol in 4 subjects only")
            return
        new_subject = Utils().get_random_subject(self.current_student.subjects)
        self.current_student.subjects.append(new_subject)
        
        self.database.write_file()
        mb.showinfo("Enrol subject" ,f"Enrolling in Subject-{new_subject.subject_id} \n" +
                    f"You are now enrolled in {self.current_student.subjects.__len__()} out of 4 subjects")
    
    def show_all_subjects(self):
        from src.views.subject_window import SubjectWindow
        for widget in self.root.winfo_children(): widget.destroy()
        SubjectWindow(self.root, self.current_student, self.database, self.current_student.subjects)
    
    def remove_subject(self):
        if(self.current_student.subjects.__len__() == 0):
            ExceptionWindow("No subjects to remove")
            return
        
        mb.showinfo("Remove subject", f"Remove Subject by ID: {self.current_student.subjects[-1].subject_id} \n" +
                    f"Dropping Subject-{self.current_student.subjects[-1].subject_id} \n")
        self.current_student.subjects.pop()
        mb.showinfo("Remove subject", f"You are now enrolled in {self.current_student.subjects.__len__()} out of 4 subjects")
        self.database.write_file()
    
    def show_login(self):
        from src.views.GUIUniApp import GUIUniApp
        for widget in self.root.winfo_children(): widget.destroy()
        GUIUniApp(self.root)
    
    def get_current_student_database(self, current_student) -> Student:
        if(self.database.student_list.__len__() == 0):
            return None
        for student in self.database.student_list:
            if student.student_id == current_student.student_id:
                return student