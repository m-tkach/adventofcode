import sys
from collections import defaultdict as dd
from iparser import read_input, hashabledict

def get_size(cube):
    size = 1
    for left, right in cube.values():
        size *= max(right - left + 1, 0)
    return size

def get_overlap(cube_1, cube_2):
    maybe_overlap = hashabledict()
    for c in cube_1:
        left_1, right_1 = cube_1[c]
        left_2, right_2 = cube_2[c]
        maybe_overlap[c] = max(left_1, left_2), min(right_1, right_2)
    return maybe_overlap

def process(data):
    cubes_count = dd(int)
    for command, new_cube in data:
        extra_cubes_count = dd(int)
        for cube, count in cubes_count.items():
            maybe_overlap = get_overlap(cube, new_cube)
            if get_size(maybe_overlap) > 0:
                extra_cubes_count[maybe_overlap] -= count
        extra_cubes_count[new_cube] += +(command == 'on')
        for cube, count in extra_cubes_count.items():
            cubes_count[cube] += count
    return sum(count * get_size(cube) for cube, count in cubes_count.items())

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
