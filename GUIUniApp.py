import tkinter as tk
from tkinter import messagebox as mb
from src.controllers.student_controller import StudentController
from src.models.database import Database
from src.common.utils import Utils
from src.models.student import Student

class GUIUniApp():
    def __init__(self, root):
        self.database = Database()
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#607b8d")
        self.current_student: Student = None
        
        self.login_frame = tk.LabelFrame(self.root, text="Login", padx=20, pady=20, fg="blue", bg="#607b8d")
        self.enrollment_frame = tk.LabelFrame(self.root, text="Enrolment", padx=20, pady=20, fg="blue", bg="#607b8d")
        self.subject_frame = tk.LabelFrame(self.root, text="Subjects", padx=20, pady=20, fg="blue", bg="#607b8d")
        
        # Login Frame
        
        self.login_frame.columnconfigure(0, weight=1)
        self.login_frame.columnconfigure(1, weight=3)
        
        email_label = tk.Label(self.login_frame, text="Email:", bg="#607b8d", fg="white", justify="left")
        email_label.grid(row=0, column=0, sticky="w", pady=5, padx=5)
        
        password_label = tk.Label(self.login_frame, text="Password:", bg="#607b8d", fg="white", justify="left")
        password_label.grid(row=1, column=0, sticky="w", pady=5, padx=5)
        
        email_text = tk.StringVar()
        email_entry = tk.Entry(self.login_frame, textvariable=email_text)
        email_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        email_entry.focus()
        
        password_text = tk.StringVar()
        password_entry = tk.Entry(self.login_frame, textvariable=password_text, show="*")
        password_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        
        clear_button = tk.Button(self.login_frame, text="Clear", command=lambda: self.clear_fields(email_text, password_text))
        clear_button.grid(row=2, column=0, pady=5, padx=5, sticky="ew")
        
        login_button = tk.Button(self.login_frame, text="Login", command=lambda: self.login(email_text, password_text))
        login_button.grid(row=2, column=1, pady=5, padx=5, sticky="ew")
        
        self.show_login()
        
        # Enrollment Frame
        
        self.enrollment_frame.columnconfigure(0, weight=1)
        self.enrollment_frame.columnconfigure(1, weight=1)
        
        enroll_button = tk.Button(self.enrollment_frame, text="Enrol subject", command=self.enrol_subject)
        enroll_button.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        
        show_enrollment_button = tk.Button(self.enrollment_frame, text="Show Enrollment", command=self.show_all_subjects)
        show_enrollment_button.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        
        remove_subject_button = tk.Button(self.enrollment_frame, text="Remove subject", command=self.remove_subject)
        remove_subject_button.grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        
        logout_button = tk.Button(self.enrollment_frame, text="Logout", command=self.show_login)
        logout_button.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        
        
        # Subject Frame
        
        
        headers = ["Subject ID", "Mark", "Grade"]
        for i, header in enumerate(headers):
            label = tk.Label(self.subject_frame, text=header, bg="#607b8d", fg="white")
            label.grid(row=0, column=i, sticky="ew")
            
        for i, subject in enumerate(self.current_student.subjects):
            subject_id = tk.Label(self.subject_frame, text=subject.subject_id, bg="#607b8d", fg="white")
            subject_id.grid(row=i+1, column=0, sticky="ew")
            
            mark = tk.Label(self.subject_frame, text=subject.mark, bg="#607b8d", fg="white")
            mark.grid(row=i+1, column=1, sticky="ew")
            
            grade = tk.Label(self.subject_frame, text=Utils.grade_calculate(subject.mark), bg="#607b8d", fg="white")
            grade.grid(row=i+1, column=2, sticky="ew")
            
        
    def clear_fields(self, email_text, password_text):
        email_text.set("")
        password_text.set("")
        
    def login(self, email_text, password_text):
        if Utils().check_email(email_text.get()) and Utils().check_password(password_text.get()):
            current_student = self.database.student_login(email_text.get(), password_text.get())
            if current_student:
                self.current_student = current_student
                mb.showinfo("Login Successful", "Welcome back, " + self.current_student.name)
                self.show_enrollment()
            else:
                print("Student does not exist")
                
    def show_enrollment(self):
        self.login_frame.pack_forget()
        self.subject_frame.pack_forget()
        self.enrollment_frame.pack(fill="both", expand="yes", padx=20, pady=20)
        
    def show_login(self):
        self.enrollment_frame.pack_forget()
        self.subject_frame.pack_forget()
        self.login_frame.pack(fill="both", expand="yes", padx=20, pady=20)
        
    def show_subject_frame(self):
        self.enrollment_frame.pack_forget()
        self.login_frame.pack_forget()
        self.subject_frame.pack(fill="both", expand="yes", padx=20, pady=20)
        
    def enrol_subject(self):
        pass
    
    def show_all_subjects(self):
        self.show_subject_frame()
    
    def remove_subject(self):
        pass
    
        
if __name__ == "__main__":
    root = tk.Tk()
    GUIUniApp(root)
    root.mainloop()