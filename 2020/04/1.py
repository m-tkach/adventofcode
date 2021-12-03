def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            yield line.strip()


def parse_passports(a):
    passports = [[]]
    for line in a:
        if not line:
            passports.append([])
        else:
            passports[-1].extend(line.split())
    structured_passports = []
    for p in passports:
        structure = {}
        for item in p:
            k, v = item.split(':')
            structure[k] = v
        structured_passports.append(structure)
    return structured_passports


def process(a):
    REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passports = parse_passports(a)
    return sum(len(REQUIRED_FIELDS & set(passport.keys())) == len(REQUIRED_FIELDS) for passport in passports)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
