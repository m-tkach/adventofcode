import sys
from iparser import read_input

def process(data):
    stacks, moves = data
    for pile_size, stack_from, stack_to in moves:
        for _ in range(pile_size):
            stacks[stack_to].append(stacks[stack_from].pop())
    return ''.join(stacks[k][-1] for k in sorted(stacks))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
