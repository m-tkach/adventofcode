import os

def parse_item(item):
    start = +(item[0] == '-')
    if item[start:].isnumeric():
        return int(item)
    return item

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield [*map(parse_item, text.split())]
