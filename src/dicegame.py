from typing import Set, Type
from abc import ABC, abstractmethod
from random import randint


class DieBase(ABC):
    def __init__(self):
        self.face: int
        self.roll()

    @abstractmethod
    def roll(self):
        ...

    def __repr__(self):
        return f"{self.face}"


class D4(DieBase):
    def roll(self):
        self.face = randint(1, 4)


class D6(DieBase):
    def roll(self):
        self.face = randint(1, 6)


class D8(DieBase):
    def roll(self):
        self.face = randint(1, 8)


d4 = D4()
d6 = D6()
d8 = D8()


class Dice:
    def __init__(self, *die_classes):
        self.__dice = [die() for die in die_classes]
        self.adjust: int = 0
        self.roll_pos: Set = set()

    def plus(self, adjust) -> None:
        self.adjust = adjust
        return self

    def roll(self):
        # checks if user has provided indices to roll
        if self.roll_pos:
            for idx in self.roll_pos:
                # rolls just the dice in specified indices
                self.__dice[idx].roll()
            else:
                # resets roll_pos
                self.roll_pos = set()
        else:
            # if user didnt specify index, roll all dice.
            for die in self.__dice:
                die.roll()

    @property
    def dice(self):
        return self.__dice

    @dice.setter
    def dice(self, value):
        raise NotImplementedError

    @property
    def total(self):
        result = 0
        for die in self.__dice:
            result += die.face

        result += self.adjust
        return result

    def to_be_rolled(self, roll_pos: list):
        to_be_rolled = set(roll_pos)
        if not all(0 <= n < len(self.__dice) for n in to_be_rolled):
            raise IndexError('The indices provided are out of range')
        else:
            self.roll_pos = to_be_rolled
        return self

    def __add_new(self, die_class):
        # requires us to return a new object

        # get class name of all the die objects of our dice
        die_names = []
        if issubclass(die_class, DieBase):
            for die in self.__dice:
                die_names.append(type(die))
            # add the extra class
            die_names += [die_class]

            # create new dice object
            new = Dice(*die_names)
            return new
        else:
            raise ValueError('Wrong die')

    def __add__(self, die_class):
        return self.__add_new(die_class)

    def __radd__(self, die_class):
        return self.__add_new(die_class)

    def __iadd__(self, die_class):
        if issubclass(die_class, DieBase):
            self.__dice += [die_class()]
            return self
        else:
            raise ValueError('Wrong die')


class DiceGameBase(ABC):
    def __init__(self):
        self.dice_board = Type[Dice]
        self._player_name: str
        self.roll_attempts: int

    @abstractmethod
    def check_winner(self):
        ...

    @abstractmethod
    def roll(self):
        ...

    @abstractmethod
    def add_dice(self, die: Type[DieBase]):
        ...

    @property
    @abstractmethod
    def total_points(self):
        ...
