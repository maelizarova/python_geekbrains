from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def count_meters(self):
        pass


class Coat(AbstractClothes):
    def __init__(self, size):
        self.size = size
        super().__init__()

    @property
    def count_meters(self):
        return self.size / 6.5 + 0.5


class Suit(AbstractClothes):
    def __init__(self, height):
        self.height = height
        super().__init__()

    @property
    def count_meters(self):
        return self.height * 2 + 0.3