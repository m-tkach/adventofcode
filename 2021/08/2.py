import sys
from random import shuffle
from iparser import read_input

SEGMENTS = [119, 36, 93, 109, 46, 107, 123, 37, 127, 111]

def get_permutation(display):
    return {c: i for i, c in enumerate(display)}

def get_segment(permutation, pattern):
    return sum(1 << permutation[c] for c in pattern)

def try_fit(permutation, patterns):
    return all(get_segment(permutation, pattern) in SEGMENTS for pattern in patterns)

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
