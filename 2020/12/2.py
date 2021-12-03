def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def process(a):
    x = y = 0
    wx = 10
    wy = -1
    DX = {'E': 1, 'W': -1}
    DY = {'S': 1, 'N': -1}
    for d, v in map(lambda s: (s[0], int(s[1:])), a):
        if d in DX:
            wx += DX.get(d, 0) * v
        elif d in DY:
            wy += DY.get(d, 0) * v
        elif d == 'F':
            x += wx * v
            y += wy * v
        else:
            assert v % 90 == 0, f'{d}, {v}'
            if d == 'L':
                v = 360 - v % 360
            for _ in range(v // 90):
                wx, wy = -wy, wx
    return abs(x) + abs(y)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
