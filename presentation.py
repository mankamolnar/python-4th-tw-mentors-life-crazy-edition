import random
from copy import deepcopy

class Presentation:

    def __init__(self, topic):
        self.mentors_att = []
        self.students_att = []
        self.topic = topic

    def fill_s(self, students):
        for i in range(0, random.randrange(1, len(students))):
            new_student = random.choice(students)
            if new_student not in self.students_att:
                self.students_att.append(new_student)

    def fill_m(self, mentors):
        for i in range(0, random.randrange(1, len(mentors))):
            new_mentor = random.choice(mentors)
            if new_mentor not in self.mentors_att:
                self.mentors_att.append(new_mentor)

    def hold_presentation(self):
        old_students = deepcopy(self.students_att)
        for members in self.students_att:
            members.knowledge_level += 2
            members.energy_level -= 1
        for ments in self.mentors_att:
            ments.energy_level -= 1
        print("12:00: \nPresetation took place about: " + self.topic)
        people_att = []
        for x in self.mentors_att:
            people_att.append(x.first_name + " " + x.last_name)
        for i in range(len(self.students_att)):
            people_att.append(self.students_att[i].first_name + " " + self.students_att[i].last_name +
                              " ; knowledge level: " + str(old_students[i].knowledge_level) +
                              " --> " + str(self.students_att[i].knowledge_level))
        print("Attedning people: ")
        for person in people_att:
            print(person)
        print()
