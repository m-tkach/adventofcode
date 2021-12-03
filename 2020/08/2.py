def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    o, v = s.split()
    return o, int(v)


def process_single(instructions):
    acc = 0
    i = 0
    used = set()
    while i not in used and i < len(instructions):
        used.add(i)
        o, v = instructions[i]
        if o == 'acc':
            acc += v
            i += 1
        if o == 'jmp':
            i += v
        if o == 'nop':
            i += 1
    return i not in used, acc


def process(a):
    instructions = list(map(parse_line, a))
    for i in range(len(instructions)):
        o, v = instructions[i]
        new_o = o
        if o == 'jmp':
            new_o = 'nop'
        if o == 'nop':
            new_o = 'jmp'
        if new_o != o:
            instructions[i] = (new_o, v)
            status, acc = process_single(instructions)
            if status:
                return acc
            instructions[i] = (o, v)
    return None


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
