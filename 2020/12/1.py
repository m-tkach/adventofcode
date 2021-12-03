def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    d, *x = s
    return d, int(''.join(x))


def process(a):
    D = 'ESWN'
    DX = {'E': 1, 'W': -1}
    DY = {'S': 1, 'N': -1}
    x = y = 0
    f = 0
    for d, v in map(parse_line, a):
        if d in D:
            x += DX.get(d, 0) * v
            y += DY.get(d, 0) * v
        elif d == 'F':
            x += DX.get(D[f], 0) * v
            y += DY.get(D[f], 0) * v
        else:
            assert v % 90 == 0, f'{d}, {v}'
            k = v // 90
            if d == 'R':
                f += k
            else:
                f -= k
            f = (f + len(D) * 100) % len(D)
    return abs(x) + abs(y)




if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
