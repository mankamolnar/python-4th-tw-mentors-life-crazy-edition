import random
from codecool_class import *


class Lama:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.softness = 10

    def pet(self):
        self.softness -= 1
        self.check_if_dead()

    def ride(self):
        self.softness -= 2
        self.check_if_dead()

    def got_massage(self):
        self.softness += 3

    def introduce_lama(self):
        print("Hi, I am %s the lama. You can pet me, or ride me to gain some energy!\nBe careful, if you ride or pet me too much, I may die!" % self.name)
        print()

    def check_if_dead(self):
        if self.softness < 1:
            print("%s is dead :(" % self.name)

    def lama_goes_insane(self, codecool_class):
        if random.choice([1, 2]) == 2:
            codecool_class.mentors = []
            codecool_class.students = []
            print("%s goes insane!! It killed the whole class!" % self.name)
            print("There are %d mentors and %d students left." %
                  (len(codecool_class.mentors), len(codecool_class.students)))
            print()
