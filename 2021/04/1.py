import sys
from iparser import read_input

def is_row_win(board, used):
    for row in board:
        if all(x in used for x in row):
            return True
    return False

def is_col_win(board, used):
    for col in zip(*board):
        if all(x in used for x in col):
            return True
    return False

def process(data):
    draw, boards = data
    used = set()
    for x in draw:
        used.add(x)
        for board in boards:
            is_bingo = is_row_win(board, used) or is_col_win(board, used)
            if is_bingo:
                board_sum = sum(y for row in board for y in row if y not in used)
                return x * board_sum

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
