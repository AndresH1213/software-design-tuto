from datetime import datetime
from msilib.schema import Error
from course import Course
from student import Student


class Enroll:
    def __init__(self, student, course, date) -> None:
        if not isinstance(student, Student):
            raise Error("Invalid student...")
        if not isinstance(course, Course):
            raise Error("Invalid course")

        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade
