def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    assert 'contains' in s, f'Line does not contain allergens: {s}'
    ing, ale = s[:-1].split(' (contains ')
    return ing.split(), ale.split(', ')


def process(a):
    a2i = {}
    ic = {}
    for ingredients, allergens in map(parse_line, a):
        for a in allergens:
            if a not in a2i:
                a2i[a] = set(ingredients)
            else:
                a2i[a] &= set(ingredients)
        for i in ingredients:
            if i not in ic:
                ic[i] = 0
            ic[i] += 1

    i2a = {}
    while True:
        to_remove = []
        for a, v in a2i.items():
            if len(v) == 1:
                x = list(v)[0]
                to_remove.append(x)
                assert x not in i2a
                i2a[x] = a
        if not to_remove:
            break
        for i in to_remove:
            for a, v in a2i.items():
                if i in v:
                    a2i[a] -= {i}
    ingredients_w_allergens = sorted((a, i) for i, a in i2a.items())
    return ','.join(i for _, i in ingredients_w_allergens)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
