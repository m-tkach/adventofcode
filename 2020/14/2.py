def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def init_mask():
    return '0' * 36


def parse_line(s):
    key, value = s.split(' = ')
    if key == 'mask':
        return 'new_mask', value
    else:
        cell = int(key[4:-1])
        return 'set_value', cell, int(value)


def set_value(memory, cell, value, mask):
    assert len(mask) == 36
    def __set_value(memory, cell, value, rev_mask, i):
        if i == 36:
            memory[cell] = value
            return
        if rev_mask[i] == '0':
            __set_value(memory, cell, value, rev_mask, i + 1)
        if rev_mask[i] == '1':
            __set_value(memory, cell | (1 << i), value, rev_mask, i + 1)
        if rev_mask[i] == 'X':
            __set_value(memory, cell, value, rev_mask, i + 1)
            __set_value(memory, cell ^ (1 << i), value, rev_mask, i + 1)
    return __set_value(memory, cell, value, mask[::-1], 0)


def process(a):
    mask = init_mask()
    memory = {}
    for item in map(parse_line, a):
        op, *rest = item
        if op == 'new_mask':
            mask = rest[0]
        else:
            cell, value = rest
            set_value(memory, cell, value, mask)
    return sum(memory.values())


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
