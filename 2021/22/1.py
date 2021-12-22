import sys
from iparser import read_input

LIMIT = 50

def process(data):
    enabled = set()
    for state, coordinates in data:
        f = enabled.add if state == 'on' else enabled.discard
        ranges = {}
        for c, (left, right) in coordinates.items():
            ranges[c] = (max(left, -LIMIT), min(right, LIMIT) + 1)
        for x in range(*ranges['x']):
            for y in range(*ranges['y']):
                for z in range(*ranges['z']):
                    f((x, y, z))
    return len(enabled)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
