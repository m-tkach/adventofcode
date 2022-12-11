import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                cmd, *val = text.split()
                if val:
                    yield (cmd, int(val[0]))
                else:
                    yield (cmd,)
