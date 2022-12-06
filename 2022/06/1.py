import sys
from iparser import read_input

def process(data):
    i = 4
    while i < len(data):
        if len({*data[i - 4:i]}) == 4:
            return i
        i += 1
    return None

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
