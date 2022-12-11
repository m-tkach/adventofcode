import sys
from iparser import read_input

CYCLE_CHECK = {*range(20, 221, 40)}

def inc_cycle(cycle, reg_x, signal_strength):
    cycle += 1
    if cycle in CYCLE_CHECK:
        signal_strength += cycle * reg_x
    return cycle, signal_strength

def process(data):
    signal_strength = 0
    cycle, reg_x = 0, 1
    for cmd, *val in data:
        if cmd == 'noop':
            cycle, signal_strength = inc_cycle(cycle, reg_x, signal_strength)
        elif cmd == 'addx':
            for _ in range(2):
                cycle, signal_strength = inc_cycle(cycle, reg_x, signal_strength)
            reg_x += val[0]
        else:
            assert False, f'Unrecognised command: {cmd}'
    return signal_strength

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
