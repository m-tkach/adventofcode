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
    total = 0
    for group in groups:
        answers, *rest_group = group
        common_answers = {*answers}
        for another_answer in rest_group:
            common_answers &= {*another_answer}
        total += len(common_answers)
    return total


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
