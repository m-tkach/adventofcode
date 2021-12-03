def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def process(a, p = 25):
    a = [*map(int, a)]
    for i, x in enumerate(a[p:]):
        b = a[i:p + i]
        if not any(x - y in b * (x != 2 * y) for y in b):
            return x


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a, 25)
    print(r)
