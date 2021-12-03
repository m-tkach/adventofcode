def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def process_case(x):
    (y, _), *x = x
    j = k = y
    for y, i in x:
        while (k + i) % y != 0:
            k += j
        j *= y
    return k


def process(a):
    _, *z = a
    res = []
    for x in z:
        x = [(int(y), i) for i, y in enumerate(x.split(',')) if y != 'x']
        res += [process_case(x)]
    return res


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(*r, sep = '\n')
