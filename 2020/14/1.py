def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def init_masks():
    return 0, (1 << 36) - 1


def parse_line(s):
    key, value = s.split(' = ')
    if key == 'mask':
        or_mask, and_mask = init_masks()
        for i, b in enumerate(value[::-1]):
            if b == '1':
                or_mask ^= 1 << i
            if b == '0':
                and_mask ^= 1 << i
        return 'new_mask', or_mask, and_mask
    else:
        cell = int(key[4:-1])
        return 'set_value', cell, int(value)


def process(a):
    or_mask, and_mask = init_masks()
    memory = {}
    for op, x, y in map(parse_line, a):
        if op == 'new_mask':
            or_mask, and_mask = x, y
        else:
            memory[x] = y & and_mask | or_mask
    return sum(memory.values())


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
