import sys
from collections import defaultdict as dd
from iparser import read_input

def diff(c1, c2):
    if c1 < c2:
        return 1
    if c1 > c2:
        return -1
    return 0

def process(data):
    field = dd(int)
    for (x1, y1), (x2, y2) in data:
        dx = diff(x1, x2)
        dy = diff(y1, y2)
        while x1 != x2 or y1 != y2:
            field[(x1, y1)] += 1
            x1 += dx
            y1 += dy
        field[(x1, y1)] += 1
    return sum(v > 1 for v in field.values())

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
