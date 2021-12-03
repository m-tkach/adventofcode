def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_ranges(a):
    ranges = {}
    for line in a:
        splitter_index = line.find(':')
        raw_ranges = line[splitter_index + 2:]
        ranges_list = []
        for item in raw_ranges.split(' or '):
            x, y = map(int, item.split('-'))
            ranges_list.append((x, y))
        range_type = line[:splitter_index]
        ranges[range_type] = ranges_list
    return ranges


def gen_valid_tickets(tickets, ranges):
    for ticket in tickets:
        values = [*map(int, ticket.split(','))]
        for v in values:
            if not any(x <= v <= y for r in ranges.values() for x, y in r):
                break
        else:
            yield values


def check_ticket_positions(tickets, index, ranges):
    for ticket in tickets:
        value = ticket[index]
        if not any(x <= value <= y for x, y in ranges):
            return False
    return True


def greedy_pairs(t2i):
    i2t = {}
    while len(i2t.keys()) < len(t2i.keys()):
        key_with_1 = None
        index_to_delete = None
        for k, v in t2i.items():
            if len(v) == 1:
                key_with_1 = k
                index_to_delete = list(v)[0]
                break
        else:
            assert False, str(t2i) + str(i2t)
        for k in t2i:
            t2i[k] -= set([index_to_delete])
        i2t[index_to_delete] = key_with_1
    return i2t


def process(a):
    a = [*a]
    yti = a.index('your ticket:')
    ranges = parse_ranges(a[:yti])
    nti = a.index('nearby tickets:')
    tickets = a[nti + 1:]
    valid_tickets = [*gen_valid_tickets(tickets, ranges)]
    ranges_keys = list(ranges.keys())
    ranges_size = len(ranges_keys)

    type2indices = {}
    for key, value in ranges.items():
        type2indices[key] = set()
        for index in range(ranges_size):
            if check_ticket_positions(valid_tickets, index, value):
                type2indices[key].add(index)
    greedy_result = greedy_pairs(type2indices.copy())

    my_ticket = [*map(int, a[yti + 1].split(','))]
    result = 1
    for i, key in greedy_result.items():
        if key.startswith('departure'):
            result *= my_ticket[i]
    return result


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
