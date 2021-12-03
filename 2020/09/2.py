def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def get_sum_and_pos(a, p = 25):
    for i, x in enumerate(a[p:]):
        b = a[i:p + i]
        if not any(x - y in b * (x != 2 * y) for y in b):
            return x, i


def process(a, p):
    a = [*map(int, a)]
    s, e = get_sum_and_pos(a, p)
    l = r = 0
    q = 0
    while r < len(a) and q != s:
        q += a[r]
        r += 1
        while q > s:
            q -= a[l]
            l += 1
    return max(a[l:r]) + min(a[l:r])


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a, 25)
    print(r)
