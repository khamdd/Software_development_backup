import re
import random
from src.models.subject import Subject

class Utils:
    EMAIL_REGEX = r'^[a-zA-Z0-9]+\.?[a-zA-Z0-9]+@university\.com$'
    PASSWORD_REGEX = r'^[A-Z][a-zA-Z]{5,}\d{3,}$'
    
    @staticmethod
    def check_email(email):
        pattern = re.compile(Utils.EMAIL_REGEX)
        return True if pattern.match(email) else False
    
    @staticmethod
    def check_password(password):
        pattern = re.compile(Utils.PASSWORD_REGEX)
        return True if pattern.match(password) else False
    
    @staticmethod
    def grade_calculate(mark: float):
        if mark >= 85:
            grade = "HD"
        elif mark >= 75:
            grade = "D"
        elif mark >= 65:
            grade = "C"
        elif mark >= 50:
            grade = "P"
        else:
            grade = "F"
        return grade
    
    @staticmethod
    def get_random_subject():
        mark = random.randint(25, 100)
        return Subject(random.randint(1, 999), mark, Utils.grade_calculate(mark))
