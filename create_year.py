import datetime
import os
import sys

INPUT_PARSER_CODE = \
'''
import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text
'''[1:]

SOLUTION_CODE = \
'''
import sys
from iparser import read_input

def process(data):
    ...
    return list(data)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
'''[1:]

def create_year_directory(year):
    aoc_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(aoc_directory)
    os.mkdir(year)
    os.chdir(year)

def create_file(filename, data):
    with open(filename, 'w') as ofs:
        ofs.write(data)

def create_day_directory(day):
    os.mkdir(day)
    os.chdir(day)
    create_file('__init__.py', '')
    for test_file_name in 'example input'.split():
        test_placeholder = test_file_name.title() + '\n'
        create_file(test_file_name + '.txt', test_placeholder)
    create_file('iparser.py', INPUT_PARSER_CODE)
    create_file('1.py', SOLUTION_CODE)
    create_file('2.py', SOLUTION_CODE)
    os.chdir('..')

def main(year):
    create_year_directory(year)
    for day in range(1, 26):
        create_day_directory(str(day).zfill(2))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        year = sys.argv[1]
    else:
        now = datetime.datetime.now()
        year = str(now.year)
    main(year)
