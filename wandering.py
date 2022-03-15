import random
from re import X

class wandering:

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def dist_origin(self):
        return (self.x**2 + self.y**2)**0.5

class commonWandering(wandering):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        dx, dy = random.choice([(0, 2), (0, -2), (2, 0), (-2, 0)])
        self.x += dx
        self.y += dy
        return [dx, dy]

class wanderingRight(wandering):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        dx, dy = random.choice([(0, 5), (5, 0), (-2, 0), (0, -2)])
        self.x += dx
        self.y += dy
        return [dx, dy]

class wanderingLeft(wandering):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        dx, dy = random.choice([(0, 2), (2, 0), (-5, 0), (0, -5)])
        self.x += dx
        self.y += dy
        return [dx, dy]