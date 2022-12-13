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

def sort_packets(packets):
    n = len(packets)
    if n < 2:
        return
    left_pile, right_pile = packets[:n//2], packets[n//2:]
    sort_packets(left_pile)
    sort_packets(right_pile)
    left_i = right_i = 0
    for i in range(n):
        if left_i >= len(left_pile) or right_i < len(right_pile) and compare(left_pile[left_i], right_pile[right_i]) != -1:
            packets[i] = right_pile[right_i]
            right_i += 1
        else:
            packets[i] = left_pile[left_i]
            left_i += 1

def process(data):
    dividers = [[[2]], [[6]]]
    packets = dividers[:]
    for datum in data:
        packets.extend(datum)
    sort_packets(packets)
    result = 1
    for i, packet in enumerate(packets, 1):
        if packet in dividers:
            result *= i
    return result

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
