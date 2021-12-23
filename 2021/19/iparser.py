import os

def read_input(filename):
    scanners = []
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text.startswith('---'):
                scanners.append([])
            elif text:
                scanners[-1].append(tuple(map(int, text.split(','))))
    return scanners
