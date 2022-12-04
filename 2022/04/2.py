import sys
from iparser import read_input

def is_overlap(left_1, right_1, left_2, right_2):
    if left_2 < left_1:
        return is_overlap(left_2, right_2, left_1, right_1)
    return right_1 >= left_2

def process(data):
    k = 0
    for elf1, elf2 in data:
        k += is_overlap(*elf1, *elf2)
    return k

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
