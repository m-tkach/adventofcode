import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    data = [*open(os.path.join(day_dir, filename), 'r')][0]
    return map(int, data.split(','))
