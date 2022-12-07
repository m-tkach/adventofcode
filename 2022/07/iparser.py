import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                p, c, *r = text.split()
                if p == '$':
                    if c == 'cd':
                        yield (c, *r)
                    elif c != 'ls':
                        assert False
                elif p == 'dir':
                    yield (p, c)
                elif p.isnumeric():
                    yield (c, int(p))
                else:
                    assert False
