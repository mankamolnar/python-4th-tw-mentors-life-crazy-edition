import random


class HeadsOrTails:

    def __init__(self, cost, win_prize):
        self.cost = cost
        self.win_prize = win_prize

    def play_game_get_result(self):
        return random.choice([0, self.win_prize])
