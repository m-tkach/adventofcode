import sys
from iparser import read_input

def inc_cycle(cycle, reg_x, crt):
    crt.append('.#'[reg_x - 1 <= cycle % 40 <= reg_x + 1])
    return cycle + 1, crt

def process(data):
    crt = []
    cycle, reg_x = 0, 1
    for cmd, *val in data:
        if cmd == 'noop':
            cycle, crt = inc_cycle(cycle, reg_x, crt)
        elif cmd == 'addx':
            for _ in range(2):
                cycle, crt = inc_cycle(cycle, reg_x, crt)
            reg_x += val[0]
        else:
            assert False, f'Unrecognised command: {cmd}'
    return '\n'.join(''.join(crt[i:i+40]) for i in range(0, len(crt), 40))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
