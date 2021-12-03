import copy
import random


class IntTileUtils:
    @staticmethod
    def convert(line):
        v = 0
        for i, c in enumerate(line[::-1]):
            v |= (c == '#') << i
        return v

    @staticmethod
    def flip(v, n):
        x = 0
        for i in range(n - 1, -1, -1):
            x |= ((v >> (n - i - 1)) & 1) << i
        return x

    @staticmethod
    def bits(vs, i):
        x = 0
        for j, v in enumerate(vs):
            x |= ((v >> i) & 1) << j
        return x

    @staticmethod
    def get_bits(v):
        total_bits = 0
        while v != 0:
            total_bits += v & 1
            v >>= 1
        return total_bits


class IntTile:
    def __init__(self, tile_id, lines):
        self.id = tile_id
        self.int_values = list(map(IntTileUtils.convert, lines))
        self.n = len(lines)

    def left(self):
        return IntTileUtils.bits(self.int_values[::-1], self.n - 1)

    def right(self):
        return IntTileUtils.bits(self.int_values[::-1], 0)

    def top(self):
        return self.int_values[0]

    def bottom(self):
        return self.int_values[-1]

    def get_current_sides(self):
        return [self.top(), self.bottom(), self.left(), self.right()]

    def get_all_sides(self):
        sides = self.get_current_sides()
        return set(sides + [IntTileUtils.flip(v, self.n) for v in sides])

    def flip_vert(self):
        self.int_values = self.int_values[::-1]

    def flip_horz(self):
        self.int_values = [IntTileUtils.flip(v, self.n) for v in self.int_values]

    def rotate_right(self):
        self.int_values = [IntTileUtils.bits(self.int_values, i) for i in range(self.n - 1, -1, -1)]

    def do_random_move(self):
        rand_move = random.choice(('flip_horz', 'flip_vert', 'rot_90', 'rot_180', 'rot_270', 'none'))
        if rand_move == 'flip_horz':
            self.flip_horz()
        elif rand_move == 'flip_vert':
            self.flip_vert()
        elif rand_move.startswith('rot'):
            angle = int(rand_move.split('_')[1])
            for _ in range(angle // 90):
                self.rotate_right()

    def get_inside_values(self):
        return [(v >> 1) & ((1 << self.get_inside_size()) - 1) for v in self.int_values[1:-1]]

    def get_inside_size(self):
        return self.n - 2


class SuperIntTile(IntTile):

    MONSTER_LINES = [2, 549255, 299592]

    def __init__(self, values):
        self.int_values = values
        self.n = len(values)
        self.id = None

    def get_monsters(self):
        result = 0
        for shift in range(self.n):
            for values in zip(self.int_values, self.int_values[1:], self.int_values[2:]):
                if all((value >> shift) & mask == mask for value, mask in zip(values, SuperIntTile.MONSTER_LINES)):
                    result += 1
        return result

    def get_bits(self):
        return sum(map(IntTileUtils.get_bits, self.int_values))


def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_int_tiles(a):
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
        objects.append(IntTile(k, v))
    return objects


def build_graph(tiles):

    def add2graph(graph, x, y):
        if x not in graph:
            graph[x] = []
        graph[x].append(y)

    sides_graph = {}
    for i, t in enumerate(tiles):
        for j, o in enumerate(tiles[i + 1:]):
           if t.get_all_sides() & o.get_all_sides():
                add2graph(sides_graph, i, j + i + 1)
                add2graph(sides_graph, j + i + 1, i)
    return sides_graph


def get_shortest_path(graph, start, end):
    q = [start]
    f = 0
    p = {start: (None, 0)}
    while f < len(q) and end not in p:
        v = q[f]
        f += 1
        _prev, dist = p[v]
        for u in graph.get(v, []):
            if u not in p:
                p[u] = (v, dist + 1)
                q.append(u)
    assert end in p
    path = [end]
    while path[-1] != start:
        last = path[-1]
        prev, _dist = p[last]
        path.append(prev)
    return path[::-1]


def graph2grid(graph, corners, grid_side):
    grid = [[None] * grid_side for _ in range(grid_side)]
    first_corner, *rest_corners = corners
    shortest_paths = sorted([get_shortest_path(graph, first_corner, other_corner) for other_corner in rest_corners], key=len)
    assert len(grid) == len(shortest_paths[0])
    grid[0][:] = shortest_paths[0]
    for i, v in enumerate(shortest_paths[1]):
        grid[i][0] = v
    last_corner = shortest_paths[-1][-1]
    for i, v in enumerate(get_shortest_path(graph, grid[0][-1], last_corner)):
        grid[i][-1] = v
    for i, line in enumerate(grid[1:]):
        grid[i + 1][:] = get_shortest_path(graph, line[0], line[-1])
    return grid


def all_tiles_stable(grid, tiles):

    def is_tile_stable(grid, i, j, tiles):
        cur_tile_index = grid[i][j]
        cur_tile = tiles[cur_tile_index]
        cur_tile_sides = cur_tile.get_current_sides()
        for side, (y, x) in enumerate(zip((i - 1, i + 1, i, i), (j, j, j - 1, j + 1))):
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
                continue
            cur_tile_side = cur_tile_sides[side]
            adj_tile_index = grid[y][x]
            adj_tile_side = tiles[adj_tile_index].get_current_sides()[side ^ 1]
            if cur_tile_side != adj_tile_side:
                return False
        return True

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not is_tile_stable(grid, i, j, tiles):
                return False
    return True


def fit_tiles(grid, tiles):

    def fit_two_tiles_horz(grid, i, j, tiles):
        curr_tile = tiles[grid[i][j]]
        next_tile = tiles[grid[i][j + 1]]
        while curr_tile.right() != next_tile.left():
            tile = random.choice([curr_tile, next_tile])
            tile.do_random_move()

    def fit_two_tiles_vert(grid, i, j, tiles):
        curr_tile = tiles[grid[i][j]]
        next_tile = tiles[grid[i + 1][j]]
        while curr_tile.bottom() != next_tile.top():
            tile = random.choice([curr_tile, next_tile])
            tile.do_random_move()

    while not all_tiles_stable(grid, tiles):
        for i, row in enumerate(grid):
            for j, tile_index in enumerate(row):
                if j + 1 < len(row):
                    fit_two_tiles_horz(grid, i, j, tiles)
                if i + 1 < len(grid):
                    fit_two_tiles_vert(grid, i, j, tiles)


def create_super_tile(grid, tiles):
    super_tile_values = []
    for i, line in enumerate(grid):
        tile_values = []
        for j, tile_index in enumerate(line):
            tile = tiles[tile_index]
            n = tile.get_inside_size()
            for k, value in enumerate(tile.get_inside_values()):
                while len(tile_values) <= k:
                    tile_values.append(0)
                tile_values[k] = (tile_values[k] << n) | value
        super_tile_values.extend(tile_values)
    return SuperIntTile(super_tile_values)


def process(a):
    tiles = parse_int_tiles(a)
    sides_graph = build_graph(tiles)
    corners = [k for k, v in sides_graph.items() if len(v) == 2]
    assert len(corners) == 4

    grid_size = int(len(tiles)**.5 + 1e-3)
    grid = graph2grid(sides_graph, corners, grid_size)
    fit_tiles(grid, tiles)

    super_tile = create_super_tile(grid, tiles)
    monsters = super_tile.get_monsters()
    while monsters == 0:
        super_tile.do_random_move()
        monsters = super_tile.get_monsters()
    return super_tile.get_bits() - monsters * sum(map(IntTileUtils.get_bits, SuperIntTile.MONSTER_LINES))


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
