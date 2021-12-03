def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_input(a):
    rules, words = {}, []
    for line in a:
        if ': ' in line:
            rule, data = line.split(': ', 1)
            if '"' in data:
                assert len(data) == 3 and data.count('"') == 2 and data[1].isalpha(), f'Unspecified data line {data}'
                value = data[1]
            else:
                ranges = data.split(' | ')
                value = [list(map(int, r.split())) for r in ranges]
            rules[int(rule)] = value
        else:
            assert len(line) == line.count('a') + line.count('b'), f'Overcomplicated string line {line}'
            words.append(line)
    return rules, words


def go(rules, rule):
    value = rules[rule]
    if type(value) is str:
        return [value]
    result = []
    for r in value:
        first_rule, *rest = r
        res_words = go(rules, first_rule)
        for next_rule in rest:
            suffixes = go(rules, next_rule)
            new_res_words = []
            for suf in suffixes:
                for w in res_words:
                    new_res_words.append(w + suf)
            res_words = new_res_words
        result.extend(res_words)
    return result


def process(a):
    rules, words = parse_input(a)
    result = set(go(rules, 0))
    return sum(word in result for word in words)


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
