from person import Person
import os
import random


class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.knowledge_level = random.randint(5, 20)

    @classmethod
    def create_by_csv(cls, path):
        with open(path, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
        list_of_students = []
        for i in range(len(table)):
            student_instance = Student(table[i][0], table[i][1], table[i][2], table[i][3])
            list_of_students.append(student_instance)
        return list_of_students

    def print_status(self):
        print("%s: \nGold coins: %d\nEnergy level: %d\nKnowledge level: %d\n" %
              (self.first_name, self.gold_coin, self.energy_level, self.knowledge_level))

    def introduce_student(self):
        print("Let's meet one of our students: ")
