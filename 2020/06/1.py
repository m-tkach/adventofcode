def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            yield line.strip()


def parse_groups(a):
    group = []
    for line in a:
        if line:
            group.append(line)
        else:
            yield group
            group = []
    if group:
        yield group


def process(a):
    groups = parse_groups(a)
    return sum(len({*''.join(group)}) for group in groups)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
