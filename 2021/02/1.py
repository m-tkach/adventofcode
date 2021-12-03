import sys
from iparser import read_input

def process(data):
    x = y = 0
    for c, v in data:
        if c == 'forward':
            x += v
        elif c == 'up':
            y -= v
        else:
            y += v
    return x * y

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
