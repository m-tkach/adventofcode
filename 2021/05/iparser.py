import os

def parse_coord(pair):
    x, y = map(int, pair.split(','))
    return x, y

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                left, right = text.split(' -> ')
                yield parse_coord(left), parse_coord(right)
