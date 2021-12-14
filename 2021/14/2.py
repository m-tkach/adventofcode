import sys
from collections import defaultdict as dd
from iparser import read_input

STEPS = 40

def process(data):
    polymer, patterns = data
    pairs = dd(int)
    for x, y in zip('^' + polymer, polymer + '$'):
        pairs[x + y] += 1
    for _step in range(STEPS):
        new_pairs = dd(int)
        for k, v in pairs.items():
            if k not in patterns:
                new_pairs[k] += v
            else:
                x, y = k
                c = patterns[k]
                new_pairs[x + c] += v
                new_pairs[c + y] += v
        pairs = new_pairs
    freq = dd(int)
    for (x, y), v in pairs.items():
        if x != '^':
            freq[x] += v
        if y != '$':
            freq[y] += v
    return max(freq.values()) - min(freq.values()) >> 1

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
