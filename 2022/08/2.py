import sys
from iparser import read_input

def is_in_grid(grid, x, y):
    return len(grid) > y >= 0 <= x < len(grid[y])

def get_distance_stats_dp(grid, x, y, dx, dy, cache):
    ck = (x, y, dx, dy)
    if ck not in cache:
        prev_y, prev_x = y + dy, x + dx
        if is_in_grid(grid, prev_x, prev_y):
            tree = grid[prev_y][prev_x]
            dist_stats = [x + 1 for x in get_distance_stats_dp(grid, prev_x, prev_y, dx, dy, cache)]
            dist_stats[tree] = 1
            cache[ck] = dist_stats
        else:
            cache[ck] = [0] * 10
    return cache[ck]

def get_length(grid, x, y, dx, dy, cache):
    dist_stats = get_distance_stats_dp(grid, x, y, dx, dy, cache)
    tree = grid[y][x]
    return min(dist_stats[tree:])

def process(data):
    cache = {}
    best_score = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            tree_score = 1
            for d in zip((-1, 1, 0, 0), (0, 0, 1, -1)):
                tree_score *= get_length(data, x, y, *d, cache)
            best_score = max(best_score, tree_score)
    return best_score

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
