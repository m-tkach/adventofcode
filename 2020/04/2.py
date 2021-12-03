def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            yield line.strip()


def parse_passports(a):

    def append_structured_data(passports, passport_items):
        if not passport_items:
            return
        structure = {}
        for item in passport_items:
            k, v = item.split(':')
            structure[k] = v
        passports.append(structure)

    structured_passports = []
    passport_items = []
    for line in a:
        if not line:
            append_structured_data(structured_passports, passport_items)
            passport_items = []
        else:
            passport_items.extend(line.split())
    append_structured_data(structured_passports, passport_items)
    return structured_passports


def process(a):
    CHECK_NUMBER = lambda value, left, right: value.isdigit() and left <= int(value) <= right
    RULES = {
        'byr': lambda x: CHECK_NUMBER(x, 1920, 2002),
        'iyr': lambda x: CHECK_NUMBER(x, 2010, 2020),
        'eyr': lambda x: CHECK_NUMBER(x, 2020, 2030),
        'hgt': lambda x: x[-2:] in ('in', 'cm') and CHECK_NUMBER(x[:-2], 59 + 91 * (x[-2:] == 'cm'), 76 + 117 * (x[-2:] == 'cm')),
        'hcl': lambda x: len(x) == 7 and x[0] == '#' and all(c in '0123456789abcdef' for c in x[1:]),
        'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(),
        'pid': lambda x: len(x) == 9 and CHECK_NUMBER(x, 0, int(1e9) - 1),
    }

    passports = parse_passports(a)
    return sum(all(field in passport and checker(passport[field]) for field, checker in RULES.items()) for passport in passports)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
