import random
from coffee_machine import *
from hot import *
from lama import *


class Person:

    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.energy_level = random.randint(5, 15)
        self.gold_coin = random.randint(10, 20)

    def drink_coffee(self, machine):
        if self.gold_coin > 0 and type(machine) == Coffee_machine:
            try:
                machine.pour_coffee()

            except (offMachineError, noBeansError):
                machine.turn_on()
                machine.fill_beans()
                self.drink_coffee(machine)

            else:
                tmp_pre_energy_level = self.energy_level
                tmp_pre_gold_coin = self.gold_coin

                self.gold_coin = self.gold_coin - 1
                self.energy_level += random.randint(3, 5)

                print("Successfull drinking.\nGold coins changed: " + str(tmp_pre_gold_coin) + " --> " + str(self.gold_coin) +
                      "\nEnergy level changed: " + str(tmp_pre_energy_level) + " --> " + str(self.energy_level) + "\n")

    def play_HOT(self, game):
        print("Initializing Heads or Tails game: ")
        if self.gold_coin > 0 and type(game) == HeadsOrTails:
            self.gold_coin -= 1
            coins_won = game.play_game_get_result()
            self.gold_coin += coins_won
            self.energy_level -= 1
            if coins_won >= 1:
                print("You have won " + str(coins_won) + " coins! Congratulations!")
            else:
                print("Sorry, you lose!")

    def pet_lama(self, lama):
        print("%s now petting %s, the lama" % (self.last_name + " " + self.first_name, lama.name))
        self.energy_level += 1
        print("Wow, that was fun, energy level boosted: %d" % self.energy_level)
        lama.pet()
        print("%s's softness level: %d" % (lama.name, lama.softness))
        print()

    def ride_lama(self, lama):
        print("%s now riding %s, the lama" % (self.last_name + " " + self.first_name, lama.name))
        self.energy_level += 3
        print("Wow, such energy boost, energy level is now: %d" % self.energy_level)
        lama.ride()
        print("%s's softness level: %d" % (lama.name, lama.softness))
        print()

    def massage_lama(self, lama):
        print("%s now massaging %s in order to regain softness!" % (self.last_name + " " + self.first_name, lama.name))
        self.energy_level -= 3
        lama.got_massage()
        print("It was exhausting, %s's energy level is now %d, but the softness of %s increased to %d" %
              (self.first_name, self.energy_level, lama.name, lama.softness))
        print()
