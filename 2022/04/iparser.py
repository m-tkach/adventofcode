import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                left, right = map(lambda s: tuple(map(int, s.split('-'))), text.split(','))
                yield (left, right)
