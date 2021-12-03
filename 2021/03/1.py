import sys
from iparser import read_input

def process(data):
    g = e = 0
    for col in zip(*data):
        z, o = map(col.count, '01')
        g = g * 2 + (o > z)
        e = e * 2 + (o < z)
    return g * e

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
