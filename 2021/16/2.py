import sys
from iparser import read_input

def bit_reverse(x, n):
    y = 0
    for i in range(n):
        y = (y << 1) | (x >> i) & 1
    return y

def parse_value(x):
    res = shift = 0
    v = 16
    while v > 15:
        v = bit_reverse(x >> shift, 5)
        res = res << 4 | v & 15
        shift += 5
    return res, shift

def process_chunks(chunks, type_id):
    def mult(a):
        r = 1
        for x in a: r *= x
        return r

    f = [sum, mult, min, max, None, int.__gt__, int.__lt__, int.__eq__]
    if type_id < 4:
        return +f[type_id](chunks)
    return +f[type_id](*chunks)

def parse_packet(x):
    type_id = bit_reverse(x >> 3, 3)
    if type_id == 4:
        res, shift = parse_value(x >> 6)
        shift += 6
    else:
        res_chunks = []
        length_id = x >> 6 & 1
        if length_id == 0:
            sub_length = bit_reverse(x >> 7, 15)
            shift = 22
            while shift < sub_length + 22:
                sub_res, sub_shift = parse_packet(x >> shift)
                shift += sub_shift
                res_chunks.append(sub_res)
        else:
            sub_count = bit_reverse(x >> 7, 11)
            shift = 18
            for sub_i in range(sub_count):
                sub_res, sub_shift = parse_packet(x >> shift)
                shift += sub_shift
                res_chunks.append(sub_res)
        res = process_chunks(res_chunks, type_id)
    return res, shift

def process_packet(p):
    bits = len(p) * 4
    x = bit_reverse(int(p, 16), bits)
    return parse_packet(x)[0]

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
