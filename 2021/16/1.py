import sys
from iparser import read_input

def bit_reverse(x, n):
    y = 0
    for i in range(n):
        y = (y << 1) | (x >> i) & 1
    return y

def parse_value_shift(x):
    shift = 0
    v = 16
    while v > 15:
        v = bit_reverse(x >> shift, 5)
        shift += 5
    return shift

def parse_packet(x):
    version = bit_reverse(x, 3)
    type_id = bit_reverse(x >> 3, 3)
    if type_id == 4:
        shift = parse_value_shift(x >> 6) + 6
    else:
        length_id = x >> 6 & 1
        if length_id == 0:
            sub_length = bit_reverse(x >> 7, 15)
            shift = 22
            while shift < sub_length + 22:
                sub_shift, sub_version = parse_packet(x >> shift)
                shift += sub_shift
                version += sub_version
        else:
            sub_count = bit_reverse(x >> 7, 11)
            shift = 18
            for sub_i in range(sub_count):
                sub_shift, sub_version = parse_packet(x >> shift)
                shift += sub_shift
                version += sub_version
    return shift, version

def process_packet(p):
    bits = len(p) * 4
    x = bit_reverse(int(p, 16), bits)
    return parse_packet(x)[1]

def process(data):
    result = []
    for p in data:
        result.append(process_packet(p))
    return '\n'.join(map(str, result))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
