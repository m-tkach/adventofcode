import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                rocks = []
                for rock_data in text.split(' -> '):
                    rocks.append(tuple(map(int, rock_data.split(','))))
                yield rocks
