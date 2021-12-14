import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    polymer, *data = open(os.path.join(day_dir, filename), 'r')
    patterns = {}
    for line in data:
        text = line.strip()
        if text:
            match, insertion = text.split(' -> ')
            patterns[match] = insertion
    return polymer.strip(), patterns
