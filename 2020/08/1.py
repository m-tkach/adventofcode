def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    o, v = s.split()
    return o, int(v)


def process(a):
    acc = 0
    instructions = list(map(parse_line, a))
    i = 0
    used = set()
    while i not in used:
        used.add(i)
        o, v = instructions[i]
        if o == 'acc':
            acc += v
            i += 1
        if o == 'jmp':
            i += v
        if o == 'nop':
            i += 1
    return acc


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
