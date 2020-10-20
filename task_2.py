from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.v

    @size.setter
    def size(self, size):
        if size > 60:
            self.v = 60
        else:
            self.v = size

    def cloth_consumption(self):
        return f'Cloth consumption for the coat is {(self.v / 6.5 + 0.5):0.2f} sq metres'


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, height):
        if height > 220:
            self.h = 220
        else:
            self.h = height

    def cloth_consumption(self):
        return f'Cloth consumption for the suit is {(2 * self.h + 0.3):0.2f} sq metres'


coat_1 = Coat(61)
print(coat_1.size)
print(coat_1.cloth_consumption())
suit_1 = Suit(220)
print(suit_1.height)
print(suit_1.cloth_consumption())
