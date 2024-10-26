import random

class Subject:
    def __init__(self, subject_id, mark, grade):
        self.subject_id = subject_id
        self.mark = mark
        self.grade = grade
        
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
        
    # Utility methods
    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "mark": self.mark,
            "grade": self.grade
        }
        
    def __str__(self):      
        return f"[ Subject::{self.subject_id} -- mark = {self.mark} -- grade = {self.grade} ]"
    
    