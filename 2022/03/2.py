import sys
from iparser import read_input

def get_priority(c):
    return ord(c) % 32 + 26 * c.isupper()

def process(data):
    result = 0
    for elf1, elf2, elf3 in zip(data, data, data):
        c, *_ = {*elf1} & {*elf2} & {*elf3}
        assert not _
        result += get_priority(c)
    return result

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
