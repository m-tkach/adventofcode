'''

   / \ / \ / \         ...
  |0,0|0,1|0,2|        ...
   \ / \ / \ / \       ...
    |1,0|1,1|1,2|      ...
   / \ / \ / \ /       ...
  |2,0|2,1|2,2|        ...
   \ / \ / \ /         ...

y, x -> dy, dx

w   ->  0, -1
nw  ->  -1, -1 if y % 2 == 0 else 0  ->  -1, (y % 2 - 1)
ne  ->  -1, 1 if y % 2 == 1 else 0   ->  -1, (y % 2)
e   ->  0, 1
se  ->  1, 1 if y % 2 == 1 else 0    ->  1, (y % 2)
sw  ->  1, -1 if y % 2 == 0 else 0   ->  1, (y % 2 - 1)

'''


DIRECTION_MOVES = {
    'w':  lambda x, y: (x - 1, y),
    'nw': lambda x, y: (x + abs(y) % 2 - 1, y - 1),
    'ne': lambda x, y: (x + abs(y) % 2, y - 1),
    'e':  lambda x, y: (x + 1, y),
    'se': lambda x, y: (x + abs(y) % 2, y + 1),
    'sw': lambda x, y: (x + abs(y) % 2 - 1, y + 1),
}


def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    moves = []
    p = ''
    for c in s:
        p += c
        if c in 'ew':
            moves.append(p)
            p = ''
    return moves


def process(a):
    positions = {}
    for moves in map(parse_line, a):
        x = y = 0
        for move in moves:
            f = DIRECTION_MOVES.get(move)
            x, y = f(x, y)
        positions[(x, y)] = 1 ^ positions.get((x, y), 0)

    for day in range(100):
        new_positions = {}
        tiles = set()
        for (x, y), v in positions.items():
            if v == 1:
                tiles.add((x, y))
                tiles.update({f(x, y) for f in DIRECTION_MOVES.values()})
        for x, y in tiles:
            k = sum(positions.get(f(x, y), 0) for f in DIRECTION_MOVES.values())
            if k in {2, 2 - positions.get((x, y), 0)}:
                new_positions[(x, y)] = 1
        positions = new_positions.copy()
    return sum(positions.values())


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
