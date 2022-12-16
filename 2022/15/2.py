import sys
from iparser import read_input

def get_distance(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    return abs(x1 - x2) + abs(y1 - y2)

def get_extreme_point(x, y, d):
    x -= d + 1
    if x < 0:
        return 0, y + x
    return x, y

def get_covered_sensors(sensors, x, y):
    return {i for i, (*sensor, d) in enumerate(sensors) if d >= get_distance((x, y), sensor)}

def process(data):
    sensors = [(*sensor, get_distance(sensor, beacon)) for sensor, beacon in data]
    for x, y, d in sensors:
        x, y = get_extreme_point(x, y, d)
        if x < 0 or y < 0:
            continue
        i, k = 0, min(y, d)
        covered_sensors = get_covered_sensors(sensors, x, y)
        while i < k and covered_sensors:
            step = 1 << 16
            while step and not covered_sensors & (cs := get_covered_sensors(sensors, x + i + step, y - i - step)):
                step >>= 1
            if step:
                i += step
                covered_sensors &= cs
            else:
                i += 1
                covered_sensors = cs
        if not covered_sensors:
            return (x + i) * 4000000 + y - i
    return None

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
