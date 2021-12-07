import sys
from iparser import read_input

def diff(data, x):
    d = 0
    for y in data:
        d += abs(x - y)
    return d

def process(data):
    data = sorted(data)
    res = diff(data, data[-1])
    for x in range(data[0], data[-1]):
        res = min(res, diff(data, x))
    return res

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
