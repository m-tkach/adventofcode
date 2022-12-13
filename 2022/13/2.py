import sys
from iparser import read_input

def get_list(value):
    if type(value) is not list:
        value = [value]
    return value

def compare(left, right):
    if type(left) == int == type(right):
        return (left > right) - (left < right)
    left, right = map(get_list, (left, right))
    i = 0
    while len(left) > i < len(right):
        if cmp := compare(left[i], right[i]):
            return cmp
        i += 1
    return (i == len(right)) - (i == len(left))

def process(data):
    DIVIDERS = [[[2]], [[6]]]
    assert all(compare(l, r) == -1 for l, r in zip(DIVIDERS, DIVIDERS[1:])), 'Const dividers should be sorted'
    packets = []
    for datum in data:
        packets.extend(datum)
    result = 1
    for position, divider in enumerate(DIVIDERS, 1):
        for packet in packets:
            if compare(packet, divider) == -1:
                position += 1
        result *= position
    return result

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
