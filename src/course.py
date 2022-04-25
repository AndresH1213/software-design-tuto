from msilib.schema import Error
from enroll import Enroll
from professor import Professor


class Course:
    def __init__(self, name, code, max_, min_, professor) -> None:
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, professor):
                    raise Error("Invalid professor...")
            self.professores = professor
        else:
            raise Error("Invalid professor...")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Error("Invalid professor...")
        self.professores.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error('Invalid Enroll...')

        if len(self.enrollments) == self.max:
            raise Error("Cannot enroll, course is full...")

        self.enrolled.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) <= self.min
