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
    return left - 1, right - 1, letter, password


def process(a):
    total = 0
    for left, right, letter, password in map(parse_line, a):
        if (password[left] == letter) ^ (password[right] == letter):
            total += 1
    return total


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
