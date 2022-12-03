import sys
from iparser import read_input

def get_priority(c):
    return ord(c) % 32 + 26 * c.isupper()

def process(data):
    result = 0
    for rucksack in data:
        n = len(rucksack) // 2
        result += sum(map(get_priority, {*rucksack[:n]} & {*rucksack[n:]}))
    return result

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
