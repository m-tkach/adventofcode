import sys
from iparser import read_input

def choice_score(c):
    return 'ABCXYZ'.find(c) % 3 + 1

def round_score(a, b):
    a, b = map(choice_score, (a, b))
    if b == a:
        return 3
    if (b - a) % 3 == 1:
        return 6
    return 0

def process(data):
    return sum(choice_score(b) + round_score(a, b) for a, b in data)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
