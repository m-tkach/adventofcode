import sys
from iparser import read_input

def choice_value(c):
    return 'ABCXYZ'.find(c) % 3

def round_score(a, b):
    a, b = map(choice_value, (a, b))
    return (a + b - 1) % 3

def process(data):
    return sum(round_score(a, b) + choice_value(b) * 3 + 1 for a, b in data)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
