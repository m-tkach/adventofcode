import sys
from iparser import read_input

def process(data):
    x = y = a = 0
    for c, v in data:
        if c == 'forward':
            x += v
            y += a * v
        elif c == 'up':
            a -= v
        else:
            a += v
    return x * y

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
