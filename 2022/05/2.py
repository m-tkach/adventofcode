import sys
from iparser import read_input

def process(data):
    stacks, moves = data
    for pile_size, stack_from, stack_to in moves:
        stacks[stack_to].extend(stacks[stack_from][-pile_size:])
        stacks[stack_from] = stacks[stack_from][:-pile_size]
    return ''.join(stacks[k][-1] for k in sorted(stacks))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
