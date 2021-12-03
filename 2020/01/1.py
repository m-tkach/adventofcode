def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def process(a):
    values = list(map(int, a))
    positions = {x: i for i, x in enumerate(values)}
    for i, x in enumerate(values):
        y = 2020 - x
        if positions.get(y, -1) > i:
            return x * y


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
