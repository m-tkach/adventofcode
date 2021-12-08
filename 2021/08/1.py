import sys
from iparser import read_input

def process(data):
    k = 0
    for _patterns, digits in data:
        for d in digits:
            if len(d) in (2, 3, 4, 7):
                k += 1
    return k

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
