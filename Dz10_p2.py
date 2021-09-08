from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    @property
    def consumption(self):
        return round((self.parameter / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def consumption(self):
        return round((2 * self.parameter) + 0.3)


coat = Coat(110)
suit = Suit(180)
print(coat.consumption)
print(suit.consumption)