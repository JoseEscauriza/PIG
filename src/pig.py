'''
The objective of Pig is to be the first player to earn 100 points. You achieve this by rolling the dice and adding which number you roll to your overall 
score. Players are permitted to roll as many times as they’d like during their turn, but beware of rolling a 1! Doing so will cost you all the points 
you’ve collected during your turn.
If you’ve racked up the points and don’t want to risk rolling a 1, you may choose to hold and keep the numbers you’ve accumulated during your turn. 
It will be up to you to decide if the risk is worth it! Once a player reaches 100 points, the game ends and that player is the winner.'''

from abc import ABC, abstractmethod
from typing import Set, Type
from dicegame import DieBase, Dice, D6, DiceGameBase
from pigart import *
from colors import *
import time
import sys
from random import randint


class Pig(DiceGameBase):
    player = 1

    def __init__(self, board: Type[Dice], name):
        self._board = board
        self._name = name
        self.score = 0
        self.current_score = 0
        self.choice = 0

    def check_winner(self):
        if self.score >= 100:
            return True
        else:
            return False

    def roll(self):
        self._board.roll()

    def check_roll(self):
        print(f'{self._name} rolled a {light_green}{self.total}{end}')
        if self.total == 1:
            self.current_score = 0
            print(f'{light_red}OINK!{end} Turn over...')
            print()
            time.sleep(1)
            self.playerpicker()
            return False
        else:
            self.current_score += self.total
            print(
                f'Current score: {light_cyan}{self.current_score}{end}')
            print()
            return True

    def playerpicker(self):
        if Pig.player == 1:
            Pig.player = 2
        else:
            Pig.player = 1

    def menu(self):
        if self.check_winner():
            print(f'{light_green}{winner}{end}')
            return False

        self.choice = input(
            f'Please select an option: {light_green}1. Roll{end} / {light_cyan}2. Hold{end} / {light_purple}3. Check points{end} / {light_red}4. Quit{end} ')

        if self.choice == '1':
            self.roll()
            if self.check_roll():
                return True
            else:
                return False

        elif self.choice == '2':
            print()
            print(f'Adding {self.current_score} to points...')
            time.sleep(0.5)
            self.score += self.current_score
            print(f'{light_green}Total points {self.score}{end}')
            self.current_score = 0
            time.sleep(1)
            print()
            if not self.check_winner():
                self.playerpicker()
            return False

        elif self.choice == '3':
            if not self.check_winner():
                print(f'You have {light_green}{self.score} points{end}')
                return True
            else:
                return False

        elif self.choice == '4':
            print(f'{light_green}{goodbye}{end}')
            sys.exit()
        else:
            print('Please choose a valid option. (1/2/3/4)')
            self.menu()

    def add_dice(self, die: Type[DieBase]):
        pass

    def ai_player(self):
        if self.score >= 100:
            return False

        turngoal = randint(7, 20)

        if self.current_score >= turngoal:
            self.score += self.current_score
            self.current_score = 0
            print(f"{light_red}{self._name} has {self.score} total points{end}")
            print()
            if self.score >= 100:
                return False
            self.playerpicker()

        elif self.current_score < turngoal:
            self.roll()
            time.sleep(1)
            if self.check_roll():
                return True
            else:
                self.current_score = 0
                return False

    @property
    def total_points(self):
        return self.score

    @property
    def dice(self):
        return self._board.dice

    @property
    def total(self):
        return self._board.total


def main():

    print(f'{light_green}{greeting}{end}')
    print()
    time.sleep(2)

    d6 = D6
    dice = Dice(d6)
    pname = input(f'Please enter your {light_white}name{end}: ')
    player1 = Pig(dice, pname)
    aiplayer = Pig(dice, 'CPU')

    print()

    while not player1.check_winner():
        while Pig.player == 1:
            if player1.menu():
                player1.menu()
            else:
                break
        else:
            if aiplayer.check_winner():
                print(f"{red}{cpuwins}{end}")
                break
            else:
                if aiplayer.ai_player():
                    aiplayer.ai_player()


if __name__ == '__main__':
    main()
