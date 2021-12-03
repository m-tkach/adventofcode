def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_ranges(a):
    r = []
    for line in a:
        r += [[]]
        splitter_index = line.find(':')
        for item in line[splitter_index + 2:].split(' or '):
            x, y = map(int, item.split('-'))
            r[-1] += [(x, y)]
    return r


def process(a):
    a = [*a]
    yti = a.index('your ticket:')
    ranges = parse_ranges(a[:yti])
    nti = a.index('nearby tickets:')
    tickets = a[nti + 1:]
    total = 0
    valid_tickets = []
    for ticket in tickets:
        values = map(int, ticket.split(','))
        for v in values:
            if not any(x <= v <= y for r in ranges for x, y in r):
                total += v
    return total


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
