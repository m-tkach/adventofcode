import sys
from iparser import read_input

def bit_criteria(dataset, mode):
    if mode == 'most':
        bit_cmp = lambda z, o: +(z <= o)
    else:
        bit_cmp = lambda z, o: +(z > o)
    col = 0
    while len(dataset) > 1:
        bits = [0, 0]
        for b in dataset:
            bit = b[col]
            bits[int(bit)] += 1
        pass_bit = str(bit_cmp(*bits))
        dataset = [b for b in dataset if b[col] == pass_bit]
        col += 1
    return int(dataset[0], 2)

def process(data):
    data = list(data)
    oxygen = bit_criteria(data, 'most')
    co2 = bit_criteria(data, 'least')
    return oxygen * co2

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
