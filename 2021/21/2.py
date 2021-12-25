import sys
from iparser import read_input

COUNTS = [0] * 10

class Player:
    def __init__(self, pos):
        self.dp = {0: {(pos, 0): 1}}

    def move(self, i):
        self.dp[i] = {}
        for die in range(3, 10):
            for (pos, points), ways in self.dp.get(i - 1, {}).items():
                if points < 21:
                    next_pos = (pos + die - 1) % 10 + 1
                    if (next_pos, points + next_pos) not in self.dp[i]:
                        self.dp[i][(next_pos, points + next_pos)] = 0
                    self.dp[i][(next_pos, points + next_pos)] += COUNTS[die] * ways

    def get_wins(self, other, is_first):
        wins = 0
        for i, states in self.dp.items():
            j = i - is_first
            for (_, points), ways in states.items():
                if points >= 21:
                    for (_, other_points), other_ways in other.dp.get(j, {}).items():
                        if other_points < 21:
                            wins += ways * other_ways
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
