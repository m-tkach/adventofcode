import sys
from random import shuffle
from iparser import read_input

SEGMENTS = [119, 36, 93, 109, 46, 107, 123, 37, 127, 111]

def get_permutation(display):
    return {c: i for i, c in enumerate(display)}

def get_segment(permutation, pattern):
    v = 0
    for c in pattern:
        v |= 1 << permutation[c]
    return v

def try_fit(permutation, patterns):
    view = set()
    for pattern in patterns:
        v = get_segment(permutation, pattern)
        if v not in SEGMENTS:
            return False
    return True

def process(data):
    display = [*'abcdefg']
    total = 0
    for patterns, digits in data:
        while not try_fit(permutation := get_permutation(display), patterns):
            shuffle(display)
        value = 0
        for digit in digits:
            value = value * 10 + SEGMENTS.index(get_segment(permutation, digit))
        total += value
    return total

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
