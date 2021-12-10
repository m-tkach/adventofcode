import sys
from iparser import read_input

def parse_line(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if abs(ord(c) - ord(stack.pop())) > 2:
                return False, 'CORRUPT', c
    if stack:
        return False, 'INCOMPLETE', ''.join(reversed(stack))
    return True, '', ''

def process(data):
    points = dict(map(reversed, enumerate(' ([{<')))
    scores = []
    for line in data:
        status, err, metadata = parse_line(line)
        if not status and err == 'INCOMPLETE':
            score = 0
            for c in metadata:
                score = score * 5 + points[c]
            scores.append(score)
    return sorted(scores)[len(scores) // 2]

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
