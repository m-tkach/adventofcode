import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    line = [*open(os.path.join(day_dir, filename), 'r')][0].strip()
    horz, vert = None, None
    for w in line.split():
        if w.startswith('x='):
            horz = tuple(map(int, w[2:-1].split('..')))
        elif w.startswith('y='):
            vert = tuple(map(int, w[2:].split('..')))
    return horz, vert
