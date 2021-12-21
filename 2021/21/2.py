import sys
from iparser import read_input

COUNTS = [0] * 10

class Player:
    def __init__(self, pos):
        self.dp = {(pos, 0, 0): 1}

    def move(self, i):
        new_dp = {}
        for d in range(3, 10):
            for x, p, j in self.dp:
                if p < 21 and j + 1 == i:
                    y = (x + d - 1) % 10 + 1
                    if (y, p + y, i) not in new_dp:
                        new_dp[(y, p + y, i)] = 0
                    new_dp[(y, p + y, i)] += COUNTS[d] * self.dp[(x, p, j)]
        self.dp.update(new_dp)

    def get_wins(self, other, is_first):
        wins = 0
        for x, q, i in self.dp:
            if q > 20:
                for y, p, j in other.dp:
                    if i == j + is_first and p < 21:
                        wins += self.dp[(x, q, i)] * other.dp[(y, p, j)]
        return wins

def process(data):
    for d1 in 1, 2, 3:
        for d2 in 1, 2, 3:
            for d3 in 1, 2, 3:
                COUNTS[d1 + d2 + d3] += 1
    a, b = [*map(Player, data)]
    for i in range(1, 15):
        a.move(i)
        b.move(i)
    return max(a.get_wins(b, 1), b.get_wins(a, 0))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
