import sys
from iparser import read_input

class Die:
    def __init__(self):
        self.val = 1
        self.k = 0

    def roll(self):
        x = self.val
        self.val += 1
        if self.val > 100:
            self.val = 1
        self.k += 1
        return x

    def count(self):
        return self.k

class Player:
    def __init__(self, pos):
        self.x = pos
        self.p = 0

    def move(self, d):
        self.x = (self.x + d - 1) % 10 + 1
        self.p += self.x

    def points(self):
        return self.p

def process(data):
    z = a, b = [*map(Player, data)]
    d = Die()
    while a.points() < 1e3 > b.points():
        z[0].move(d.roll() + d.roll() + d.roll())
        z = z[::-1]
    return min(a.points(), b.points()) * d.count()

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
