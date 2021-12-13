import sys
from iparser import read_input

def fold(points, fold_c, axis):
    folded_points = set()
    c_index = +(axis == 'y')
    for p in points:
        c = p[c_index]
        if c >= fold_c:
            p = list(p)
            p[c_index] = 2 * fold_c - c
            p = tuple(p)
        folded_points.add(p)
    return list(folded_points)

def max_dim(points, dim):
    return max(points, key = lambda p: p[dim])[dim] + 1

def get_canvas(points):
    canvas = [[' '] * max_dim(points, 0) for _ in range(max_dim(points, 1))]
    for x, y in points:
        canvas[y][x] = '#'
    return '\n'.join(''.join(line) for line in canvas)

def process(data):
    points, folds = data
    for axis, fold_c in folds:
        points = fold(points, fold_c, axis)
    return get_canvas(points)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
