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
        yield x.split(' ', 1)[1], a


def process(a):
    def dfs(g, v, u):
        k = 1
        for x in g.get(v, []):
            if x not in u:
                u.add(x)
                k += dfs(g, x, u)
        return k

    g = {}
    for s in a:
        for x, y in parse_line(s):
            if x not in g: g[x] = []
            g[x].append(y)
    k = dfs(g, 'shiny gold bag', set())
    return k - 1


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
