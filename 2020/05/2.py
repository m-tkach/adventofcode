def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    b = ''.join('01'[c in 'BR'] for c in s)
    return int(b, 2)


def process(a):
    seats = sorted(map(parse_line, a))
    for x, y in zip(seats, seats[1:]):
        if y - x != 1:
            assert y - x == 2
            return (x + y) // 2


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
