import random
from src.models.subject import Subject
from typing import List

class Student:
    def __init__(self, student_id, name, email, password, subjects):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects: List[Subject] = subjects
    
    # Getters
    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password
    
    @property
    def subjects(self):
        return self._subjects

    # Setters
    @name.setter
    def name(self, name):
        self._name = name

    @email.setter
    def email(self, email):
        self._email = email
        
    @password.setter
    def password(self, password):
        self._password = password
    
    @subjects.setter
    def subjects(self, subjects):
        self._subjects = subjects

    # Utility methods
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}, Subjects: {self.subjects}"
    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": [subject.to_dict() for subject in self.subjects]
        }
