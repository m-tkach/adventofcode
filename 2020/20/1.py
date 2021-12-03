class Tile:
    def __init__(self, tile_id, lines):
        self.id = tile_id
        self.lines = lines
        self.sides = [lines[0], lines[-1], ''.join(line[0] for line in lines), ''.join(line[-1] for line in lines)]
        self.rev_sides = [lines[0][::-1], lines[-1][::-1], ''.join(line[0] for line in lines[::-1]), ''.join(line[-1] for line in lines[::-1])]

    def sides(self):
        return self.sides

    def rev_sides(self):
        return self.rev_sides

    def all_sides(self):
        return self.sides + self.rev_sides

    def get_id(self):
        return self.id

    def side_match(self, side):
        return side in self.sides + self.rev_sides


def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_tiles(a):
    tiles = {}
    latest_tile = None
    for line in a:
        if 'Tile' in line:
            latest_tile = int(''.join(filter(str.isdigit, line)))
            tiles[latest_tile] = []
        else:
            tiles[latest_tile].append(line)
    objects = []
    for k, v in tiles.items():
        objects.append(Tile(k, v))
    return objects


def process(a):
    tiles = parse_tiles(a)
    ids = []
    for i, t in enumerate(tiles):
        k = 0
        for j, o in enumerate(tiles):
            if i == j:
                continue
            for s in t.all_sides():
                if o.side_match(s):
                    k += 1
                    break
        if k == 2:
            ids.append(t.get_id())
    assert len(ids) == 4, f'We have more/less valid tile ids in corners: {len(ids)}'
    r, *other_ids = ids
    for i in other_ids:
        r *= i
    return r


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
