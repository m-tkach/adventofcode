def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def process(a):
    t, x = a
    t = int(t)
    bd = 1e18
    by = None
    for y in map(int, filter(lambda y: y != 'x', x.split(','))):
        d = y - t % y
        if d < bd:
            bd, by = d, y
    return bd * by


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
