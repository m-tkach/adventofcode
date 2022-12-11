import os

'''
return s a list monkeys, where each monkey is a tuple of (id, list of items, operation, div_test, true_monkey, false_monkey)
'''
def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        monkeys = []
        monkey = None
        for line in ifs:
            text = line.strip()
            if not text:
                if monkey:
                    monkeys.append(tuple(monkey))
                    monkey = None
                continue
            if text.startswith('Monkey'):
                monkey = []
                monkey.append(int(text[7:-1]))
            elif text.startswith('Starting items'):
                assert monkey
                monkey.append(list(map(int, text[16:].split(','))))
            elif text.startswith('Operation'):
                assert monkey
                monkey.append(eval('lambda old: ' + text[17:]))
            elif text.startswith('Test'):
                assert monkey
                assert 'divisible by' in text
                monkey.append(int(text[19:]))
            elif text.startswith('If true'):
                assert monkey
                monkey.append(int(text[25:]))
            elif text.startswith('If false'):
                assert monkey
                monkey.append(int(text[26:]))
            else:
                assert False, f'Unrecognised input: {text}'
        if monkey:
            monkeys.append(tuple(monkey))
        return monkeys
