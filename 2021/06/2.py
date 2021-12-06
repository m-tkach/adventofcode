import sys
from iparser import read_input

def process(data):
    school = [0] * 9
    for x in data:
        school[x] += 1
    for _day in range(256):
        new_school = [0] * 6 + [school[0], 0, school[0]]
        for cycle, fish in enumerate(school[1:]):
            new_school[cycle] += fish
        school = new_school
    return sum(school)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
