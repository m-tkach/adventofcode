import sys
from iparser import read_input

LINE_NUMBERS = {10, 2000000}

def process(data):
    chunks = {y: [] for y in LINE_NUMBERS}
    for (sensor_x, sensor_y), (beacon_x, beacon_y) in data:
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        for y in LINE_NUMBERS:
            sensor_gap = abs(sensor_y - y)
            if sensor_gap <= distance:
                delta_x = distance - sensor_gap
                chunks[y].append((sensor_x - delta_x, sensor_x + delta_x))
    results = {}
    for y, intervals in chunks.items():
        last_end = -int(1e18)
        results[y] = 0
        for start_x, end_x in sorted(intervals):
            if end_x > last_end:
                results[y] += end_x - max(start_x, last_end)
                last_end = end_x
    return '\n'.join(f"Line {k}: {v}" for k, v in sorted(results.items()))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
