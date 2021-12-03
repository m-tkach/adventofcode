def read_file(fp):
    a = []
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                a.append(text)
    return a


def parse_line(s):
    a, b = s.replace('bags', 'bag').split(' contain ')
    for x in b[:-1].split(', '):
        if 'no other bag' in x:
            continue
        k, z = x.split(' ', 1)
        yield a, z, int(k)


def process(a):
    def dfs(g, v, m = 1):
        k = m
        for x, c in g.get(v, []):
            k += dfs(g, x, c * m)
        return k

    g = {}
    for s in a:
        for x, y, c in parse_line(s):
            if x not in g: g[x] = []
            g[x].append((y, c))
    k = dfs(g, 'shiny gold bag')
    return k - 1


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
