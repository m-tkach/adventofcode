import sys
from iparser import read_input

def get_distance(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    return abs(x1 - x2) + abs(y1 - y2)

def process(data):
    sensors = [(*sensor, get_distance(sensor, beacon)) for sensor, beacon in data]
    for x, y, d in sensors:
        y -= d + 1
        if y < 0:
            x -= abs(y)
            y = 0
        for i in range(d + 1):
            if all(dist < get_distance((x, y), other_sensor) for *other_sensor, dist in sensors):
                return x * 4000000 + y
            x -= 1
            if x < 0:
                break
            y += 1
    return None

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
