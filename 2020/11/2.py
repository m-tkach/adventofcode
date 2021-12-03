def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def dp(a, y, x, dy, dx, memo):
    x += dx
    y += dy
    if not (0 <= y < len(a) and 0 <= x < len(a[y])):
        return 0
    if (y, x, dy, dx) in memo:
        return memo[(y, x, dy, dx)]
    result = 0
    if a[y][x] == '.':
        result = dp(a, y, x, dy, dx, memo)
    if a[y][x] == '#':
        result = 1
    memo[(y, x, dy, dx)] = result
    return result


def occupied(a, i, j, memo):
    k = 0
    for dy in -1, 0, 1:
        for dx in -1, 0, 1:
            if dx == 0 and dy == 0:
                continue
            k += dp(a, i, j, dy, dx, memo)
    return k


def process(a):
    a = [list(line) for line in a]
    is_changed = True
    while is_changed:
        b = []
        memo = {}
        is_changed = False
        for i, line in enumerate(a):
            z = []
            for j, s in enumerate(line):
                p = s
                occ = occupied(a, i, j, memo)
                if s == 'L' and occ == 0:
                    p = '#'
                    is_changed = True
                if s == '#' and occ >= 5:
                    p = 'L'
                    is_changed = True
                z += [p]
            b += [z]
        a = b[:]
    return sum(line.count('#') for line in a)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
