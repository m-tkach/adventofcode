def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def process(a):
    a = sorted(map(int, a))
    d = [0] * 4
    for x, y in zip([0] + a, a + [a[-1] + 3]):
        z = y - x
        assert z < 4, f'{x}, {y}'
        d[z] += 1
    return d[3] * d[1]


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
