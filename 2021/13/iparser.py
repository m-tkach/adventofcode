import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    points, folds = [], []
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text.startswith('fold along'):
                axis, value = text.split()[-1].split('=')
                folds.append((axis, int(value)))
            elif ',' in text:
                points.append(tuple(map(int, text.split(','))))
    return points, folds
