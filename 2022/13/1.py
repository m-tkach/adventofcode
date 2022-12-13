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
    result = 0
    for i, (left, right) in enumerate(data, 1):
        if compare(left, right) == -1:
            result += i
    return result

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
