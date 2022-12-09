import sys
from iparser import read_input

def head_move(head_x, head_y, move, dist):
    head_x += dist * ((move == 'R') - (move == 'L'))
    head_y += dist * ((move == 'D') - (move == 'U'))
    return head_x, head_y

def coord_dist(c1, c2):
    return c1 - c2

def tail_move(tail_x, tail_y, head_x, head_y):
    val_add = lambda v: (v < 0) - (v > 0)
    return tuple(t + val_add(coord_dist(t, h)) for t, h in zip((tail_x, tail_y), (head_x, head_y)))

def knot_dist(tail_x, tail_y, head_x, head_y):
    x_diff, y_diff = (coord_dist(*i) for i in zip((head_x, head_y), (tail_x, tail_y)))
    return max(abs(x_diff), abs(y_diff))

def process(data):
    head_x, head_y, tail_x, tail_y = [0] * 4
    tail_positions = set([(tail_x, tail_y)])
    for move, dist in data:
        head_x, head_y = head_move(head_x, head_y, move, dist)
        while knot_dist(head_x, head_y, tail_x, tail_y) > 1:
            tail_x, tail_y = tail_move(tail_x, tail_y, head_x, head_y)
            tail_positions.add((tail_x, tail_y))
    return len(tail_positions)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
