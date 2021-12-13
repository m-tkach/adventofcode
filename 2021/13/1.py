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

def process(data):
    points, folds = data
    axis, fold_c = folds[0]
    points = fold(points, fold_c, axis)
    return len(points)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
