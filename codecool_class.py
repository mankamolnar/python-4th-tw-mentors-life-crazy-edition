from mentor import Mentor
from student import Student
from datetime import date
import os


class CodecoolClass:

    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):
        return CodecoolClass("Budapest", date.today().year, Mentor.create_by_csv(CodecoolClass.path + "/data/mentors.csv"),
                             Student.create_by_csv(CodecoolClass.path + "/data/students.csv"))

    def find_student_by_full_name(self, full_name):
        if type(full_name) == str:
            full_name = full_name.strip().split(" ")

            if type(full_name) == list and len(full_name) == 2:
                for student in self.students:

                    if student.first_name == full_name[0] and student.last_name == full_name[1]:
                        return student

    def find_mentor_by_full_name(self, full_name):
        if type(full_name) == str:
            full_name = full_name.strip().split(" ")

            if type(full_name) == list and len(full_name) == 2:
                for mentor in self.mentors:

                    if mentor.first_name == full_name[0] and mentor.last_name == full_name[1]:
                        return mentor

    def print_welcome_message(self):
        print("Codecool class is founded at %s in %d." % (self.location, self.year))
        print("Hello birds! Hi trees!\n")

    def print_goodbye_message(self):
        print("What a day! Now it's time to go home. See you guys!!!")
