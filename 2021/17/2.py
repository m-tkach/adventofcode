import sys
from iparser import read_input

def simulate(vel_x, vel_y, x_min, x_max, y_min, y_max):
    x = y = 0
    while abs(x) <= max(abs(x_min), abs(x_max)) and y >= y_min:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return 1
        x += vel_x
        y += vel_y
        vel_x += [-1, 0, 1][(vel_x < 0) + (vel_x <= 0)]
        vel_y -= 1
    return 0

def process(data):
    (x_min, x_max), (y_min, y_max) = data
    total = 0
    for vel_x in range(-999, 999):
        for vel_y in range(-999, 999):
            total += simulate(vel_x, vel_y, x_min, x_max, y_min, y_max)
    return total

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
