import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        _stack_lines = []
        _stack_names = None
        moves = []
        for line in ifs:
            text = line.rstrip()
            if not text:
                continue
            elif '[' in text:
                _stack_lines.append(list(text[1::4]))
            elif text.startswith('move'):
                moves.append(tuple(map(int,text.split()[1::2])))
            else:
                _stack_names = list(map(int, filter(bool, text.split())))
        stacks = {s: [] for s in _stack_names}
        for l in _stack_lines:
            for v, s in zip(l, _stack_names):
                if v != ' ':
                    stacks[s].append(v)
        return {k: v[::-1] for k, v in stacks.items()}, moves
