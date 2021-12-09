import sys
from iparser import read_input

DELTA = [-1, 1, 0, 0]

def gen_neighbors(heatmap, x, y):
    for dx, dy in zip(DELTA, reversed(DELTA)):
        if 0 <= y + dy < len(heatmap) and 0 <= x + dx < len(heatmap[y]):
            yield heatmap[y + dy][x + dx]

def process(heatmap):
    total = 0
    for y, row in enumerate(heatmap):
        for x, value in enumerate(row):
            if value < min(gen_neighbors(heatmap, x, y)):
                total += value + 1
    return total

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
