from mentor import Mentor
from student import Student
import random
from copy import deepcopy


class YogaSession:

    def __init__(self, date, type_of_yoga):
        self.date = date
        self.type_of_yoga = type_of_yoga
        self.people = []
        self.price = 5

    def add_to_session(self, students, mentors):
        for i in range(0, random.randrange(0, len(mentors))):
            mentor = random.choice(mentors)
            if mentor.gold_coin >= 5:
                if mentor not in self.people:
                    self.people.append(mentor)
        for i in range(0, random.randrange(1, len(students))):
            student = random.choice(students)
            if student.gold_coin >= 5:
                if student not in self.people:
                    self.people.append(student)

    def do_yoga(self):
        old_yogis = deepcopy(self.people)
        print("Yoga succesfully took place. Energy levels boosted as follows: ")
        for i in range(len(self.people)):
            self.people[i].energy_level += 5
            self.people[i].gold_coin -= 5
            print(self.people[i].first_name + " " + self.people[i].last_name + " ; energy level: " +
                  str(old_yogis[i].energy_level) + " --> " + str(self.people[i].energy_level))
        print()

    def print_status(self):
        print("You can join our %s yoga class on %s." % (self.type_of_yoga, self.date))
        print()
