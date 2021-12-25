import sys
from iparser import read_input

def is_taken(value, *sea_cucumber_sets):
    for sea_cucumber_set in sea_cucumber_sets:
        if value in sea_cucumber_set:
            return True
    return False

def process(data):
    n, m = len(data), len(data[0])
    east_faced, south_faced = set(), set()
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == '>':
                east_faced.add((x, y))
            elif cell == 'v':
                south_faced.add((x, y))
    has_moved = True
    steps = 0
    while has_moved:
        steps += 1
        has_moved = False
        new_east_faced, new_south_faced = set(), set()
        for x, y in east_faced:
            next_x = (x + 1) % m
            if is_taken((next_x, y), east_faced, south_faced):
                new_east_faced.add((x, y))
            else:
                has_moved = True
                new_east_faced.add((next_x, y))
        east_faced = new_east_faced
        for x, y in south_faced:
            next_y = (y + 1) % n
            if is_taken((x, next_y), east_faced, south_faced):
                new_south_faced.add((x, y))
            else:
                has_moved = True
                new_south_faced.add((x, next_y))
        south_faced = new_south_faced
    return steps

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
