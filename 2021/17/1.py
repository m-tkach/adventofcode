import sys
from iparser import read_input

def process(data):
    (_x_min, _x_max), (y_min, _y_max) = data
    return y_min *-~ y_min >> 1

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
