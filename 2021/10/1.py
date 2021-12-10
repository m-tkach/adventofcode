import sys
from iparser import read_input

def parse_line(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(ord(c))
        else:
            if abs(ord(c) - stack.pop()) > 2:
                return False, 'CORRUPT', c
    if stack:
        return False, 'INCOMPLETE', ''
    return True, '', ''

def process(data):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total = 0
    for line in data:
        status, err, metadata = parse_line(line)
        if not status and err == 'CORRUPT':
            total += points[metadata]
    return total

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
