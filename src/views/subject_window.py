import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import tkinter as tk
from src.common.utils import Utils

class SubjectWindow:
    def __init__(self, root, current_student, database, subjects):
        self.root = root
        self.subjects = subjects
        self.current_student = current_student
        self.database = database
        
        self.subject_frame = tk.LabelFrame(self.root, text="Subjects", padx=20, pady=20, fg="blue", bg="#607b8d")
        self.subject_frame.pack(fill="both", expand="yes", padx=20, pady=20)
        self.subject_frame.columnconfigure(0, weight=1)
        self.subject_frame.columnconfigure(1, weight=1)
        self.subject_frame.columnconfigure(2, weight=1)
        
        self.last_column_index = 0
        
        headers = ["Subject ID", "Mark", "Grade"]
        for i, header in enumerate(headers):
            label = tk.Label(self.subject_frame, text=header, bg="green", fg="black")
            label.grid(row=0, column=i, sticky="ew")
            
        for i, subject in enumerate(self.subjects):
            subject_id = tk.Label(self.subject_frame, text=subject.subject_id, bg="#F2F2F2", fg="black")
            subject_id.grid(row=i+1, column=0, sticky="ew")
            
            mark = tk.Label(self.subject_frame, text=subject.mark, bg="#FFFFFF", fg="black")
            mark.grid(row=i+1, column=1, sticky="ew")
            
            grade = tk.Label(self.subject_frame, text=Utils.grade_calculate(subject.mark), bg="#F2F2F2", fg="black")
            grade.grid(row=i+1, column=2, sticky="ew")
            
            
            self.last_column_index = i + 1
            
        back_button = tk.Button(self.subject_frame, text="Back", command=self.back)
        back_button.grid(row=self.last_column_index + 1, column=1, pady=5, padx=5, sticky="ew")
            
    def back(self):
        from src.views.enrolment_window import EnrolmentWindow
        for widget in self.root.winfo_children(): widget.destroy()
        EnrolmentWindow(self.root, self.current_student, self.database)