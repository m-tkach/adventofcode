import os
import re

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall("-?\d+", text))
                yield (sensor_x, sensor_y), (beacon_x, beacon_y)
