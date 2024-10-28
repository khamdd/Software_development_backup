import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import tkinter as tk
from tkinter import messagebox as mb
from src.controllers.student_controller import StudentController
from src.models.database import Database
from src.common.utils import Utils
from src.models.student import Student
from src.views.exception_window import ExceptionWindow

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
        self.login_frame.pack(fill="both", expand="yes", padx=20, pady=20)
        
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
            
        
    def clear_fields(self, email_text, password_text):
        email_text.set("")
        password_text.set("")
        
    def login(self, email_text, password_text):
        from src.views.enrolment_window import EnrolmentWindow
        
        if Utils().check_email(email_text.get()) and Utils().check_password(password_text.get()):
            current_student = self.database.student_login(email_text.get(), password_text.get())
            if current_student:
                self.current_student = current_student
                mb.showinfo("Login Successful", "Welcome back, " + self.current_student.name)
                for widget in self.root.winfo_children(): widget.destroy()
                EnrolmentWindow(self.root, self.current_student, self.database)
            else:
                ExceptionWindow("Student does not exist")
        else:
            ExceptionWindow("Invalid email or password")
    
        
if __name__ == "__main__":
    root = tk.Tk()
    GUIUniApp(root)
    root.mainloop()