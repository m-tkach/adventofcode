import sys
from iparser import read_input

def inp(state, var, val):
    state[var] = val

def add(state, var, val):
    state[var] += val

def mul(state, var, val):
    state[var] *= val

def div(state, var, val):
    q, r = divmod(state[var], val)
    state[var] = q + (r != 0 and q < 0)

def mod(state, var, val):
    state[var] %= val

def eql(state, var, val):
    state[var] = +(state[var] == val)

F = {
    'inp': inp,
    'add': add,
    'mul': mul,
    'div': div,
    'mod': mod,
    'eql': eql,
}.get

def op(state, f, var, val):
    eval_var = lambda v: ord(v) - 119
    eval_val = lambda v: v if type(v) == int else state[eval_var(v)]
    F(f)(state, eval_var(var), eval_val(val))

def expand_alus(alus, f, var):
    alu_states = {}
    for monad, state in alus:
        op(state, f, var, 0)
        state_hash = tuple(state)
        alu_states[state_hash] = max(monad, alu_states.get(state_hash, monad))
    new_alus = []
    for state_hash, monad in alu_states.items():
        for new_digit in range(1, 10):
            new_state = list(state_hash)
            op(new_state, f, var, new_digit)
            new_alus.append((monad * 10 + new_digit, new_state))
    return new_alus

def update_alus(alus, f, var, val):
    for _, state in alus:
        op(state, f, var, val)

def process(data):
    data = [*data][::-1]
    alus = [(0, 4 * [0])]
    while data:
        f, var, *val = data.pop()
        if val:
            update_alus(alus, f, var, val[0])
        else:
            alus = expand_alus(alus, f, var)
            print(f'Processing {len(alus)} ALUs (digit #{len(str(alus[0][0]))})')
    return max(monad for monad, state in alus if state[-1] == 0)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
