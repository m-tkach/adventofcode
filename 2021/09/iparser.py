import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    heatmap = []
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                heatmap.append([*map(int, text)])
    return heatmap
