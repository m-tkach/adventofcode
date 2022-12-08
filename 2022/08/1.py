import sys
from iparser import read_input

def is_in_grid(grid, x, y):
    return len(grid) > y >= 0 <= x < len(grid[y])

def get_prev_max_dp(grid, x, y, dx, dy, cache):
    ck = (x, y, dx, dy)
    if ck not in cache:
        prev_y, prev_x = y + dy, x + dx
        if is_in_grid(grid, prev_x, prev_y):
            cache[ck] = max(grid[prev_y][prev_x], get_prev_max_dp(grid, prev_x, prev_y, dx, dy, cache))
        else:
            cache[ck] = -1
    return cache[ck]

def is_visible(grid, x, y, dx, dy, cache):
    return grid[y][x] > get_prev_max_dp(grid, x, y, dx, dy, cache)

def process(data):
    cache = {}
    total = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            total += any(is_visible(data, x, y, *d, cache) for d in zip((-1, 1, 0, 0), (0, 0, 1, -1)))
    return total

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
