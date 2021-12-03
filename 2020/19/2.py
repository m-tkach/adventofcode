RULES_OVERWRITES = {
    8: [[42], [42, 8]],
    11: [[42, 31], [42, 11, 31]],
}

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
    for rule, value in RULES_OVERWRITES.items():
        rules[rule] = value
    return rules, words


def go(rules, rule, word, level):
    value = rules[rule]
    if type(value) is str:
        return {value}
    if level < 0:
        return set()
    result = set()
    for r in value:
        first_rule, *rest = r
        res_words = go(rules, first_rule, word, level - 1)
        if not res_words:
            continue
        for next_rule in rest:
            suffixes = go(rules, next_rule, word, level - 1)
            new_res_words = set()
            for suf in suffixes:
                for w in res_words:
                    new_word = w + suf
                    if new_word in word:
                        new_res_words.add(new_word)
            res_words = new_res_words
        result.update(res_words)
    return result


def process(a):
    rules, words = parse_input(a)
    total = 0
    for word in words:
        print(f'Process word #{words.index(word)} (out of {len(words)}): {word}')
        result = go(rules, 0, word, len(word))
        total += word in result
    return total


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
