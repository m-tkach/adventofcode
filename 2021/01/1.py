import sys
from iparser import read_input

def process(data):
    p, *a = data
    k = 0
    for x in a:
        k += x > p
        p = x
    return k

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
