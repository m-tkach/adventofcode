def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    info, password = s.split(': ')
    occ_range, letter = info.split()
    left, right = map(int, occ_range.split('-'))
    return left, right, letter, password


def process(a):
    total = 0
    for left, right, letter, password in map(parse_line, a):
        if left <= password.count(letter) <= right:
            total += 1
    return total


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
