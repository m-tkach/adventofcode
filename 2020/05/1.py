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
    return max(map(parse_line, a))


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
