import sys
from operator import itemgetter
from iparser import read_input

def gen_new_sand_point():
    return 500, 0

def gen_next_sand_position(points, sand_x, sand_y):
    for dx in 0, -1, 1:
        next_sand_point = sand_x + dx, sand_y + 1
        if next_sand_point not in points:
            return next_sand_point
    return None

def sign(v):
    return (v > 0) - (v < 0)

def gen_points(start, end):
    x, y = start
    end_x, end_y = end
    dx, dy = sign(end_x - x), sign(end_y - y)
    points = {end}
    while (x, y) != end:
        points.add((x, y))
        x += dx
        y += dy
    return points

def process(data):
    points = set()
    for rocks in data:
        for rock1, rock2 in zip(rocks, rocks[1:]):
            points.update(gen_points(rock1, rock2))
    y_limit = max(map(itemgetter(1), points))
    sand_count = 0
    sand_x, sand_y = gen_new_sand_point()
    while sand_y <= y_limit:
        next_sand_point = gen_next_sand_position(points, sand_x, sand_y)
        if next_sand_point:
            sand_x, sand_y = next_sand_point
        else:
            sand_count += 1
            points.add((sand_x, sand_y))
            sand_x, sand_y = gen_new_sand_point()
    return sand_count

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
