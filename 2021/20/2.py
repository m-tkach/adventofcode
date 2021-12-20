import sys
from iparser import read_input

STEPS = 50

def f_dim(a, f, d):
    return f(i[d] for i in a)

def process(data):
    algo, image = data
    empty = 0
    marks = set()
    for y, row in enumerate(image):
        for x, point in enumerate(row):
            if point == '#':
                marks.add((x, y))
    for step in range(STEPS):
        empty = [0, len(algo) - 1][algo[empty] == '#']
        min_x, max_x = f_dim(marks, min, 0), f_dim(marks, max, 0)
        min_y, max_y = f_dim(marks, min, 1), f_dim(marks, max, 1)
        new_marks = set()
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                value = 0
                for dy in -1, 0, 1:
                    for dx in -1, 0, 1:
                        mark = +((x + dx, y + dy) in marks)
                        if not mark and not (min_x <= x + dx <= max_x and min_y <= y + dy <= max_y):
                            mark = +(algo[empty] == '#')
                        value = value << 1 | mark
                is_new_mark = algo[value] == '#'
                if is_new_mark:
                     new_marks.add((x, y))
        marks = new_marks
    return len(marks)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
