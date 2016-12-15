from person import Person
import os


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, path):
        with open(path, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
        list_of_mentors = []
        for i in range(len(table)):
            mentor_instance = Mentor(table[i][0], table[i][1], table[i][2], table[i][3], table[i][4])
            list_of_mentors.append(mentor_instance)
        return list_of_mentors

    def print_status(self):
        print("%s: \nGold coins: %d\nEnergy level: %d\n" % (self.first_name, self.gold_coin, self.energy_level))

    def introduce_mentor(self):
        print("Let's meet one of our mentors: ")
