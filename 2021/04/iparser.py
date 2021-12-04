import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    raw_draw, *board_data = open(os.path.join(day_dir, filename), 'r')
    draw = [*map(int, raw_draw.split(','))]
    boards = []
    for line in board_data:
        text = line.strip()
        if text:
            boards[-1].append([*map(int, text.split())])
        else:
            boards.append([])
    return draw, boards
