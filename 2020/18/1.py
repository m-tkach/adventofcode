def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    items = ['']
    for c in s:
        if c == ' ':
            pass
        elif c.isdigit():
            items[-1] += c
        else:
            items += [c, '']
    return [*filter(lambda s: s != '', items)]


def process_line(s):

    def __apply_op(left, right, cur_op):
        if cur_op is None:
            result = right
        elif cur_op == '+':
            result = left + right
        elif cur_op == '*':
            result = left * right
        else:
            assert False, f'Unknown op: {cur_op}'
        return result

    def __eval_impl(items, start):
        result = 0
        cur_op = None
        while start < len(items):
            item = items[start]
            if item.isdigit():
                result = __apply_op(result, int(item), cur_op)
                cur_op = None
            elif item in '+*':
                cur_op = item
            elif item == '(':
                item, start = __eval_impl(items, start + 1)
                result = __apply_op(result, item, cur_op)
            elif item == ')':
                break
            start += 1
        return result, start

    items = parse_line(s)
    result, _last_pos = __eval_impl(items, 0)
    assert _last_pos == len(items), f'Eval for {s} did not compute eveything and stopped at index {_last_pos}'
    return result


def process(a):
    return sum(map(process_line, a))


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
