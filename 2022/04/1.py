import sys
from iparser import read_input

def is_full_overlap(left, right, sub_left, sub_right):
    return left <= sub_left and right >= sub_right

def process(data):
    k = 0
    for elf1, elf2 in data:
        k += is_full_overlap(*elf1, *elf2) or is_full_overlap(*elf2, *elf1)
    return k

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
