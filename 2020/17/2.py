def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_grid(a):
    grid = {}
    for y, line in enumerate(a):
        for x, c in enumerate(line):
            if c == '#':
                grid[(x, y, 0, 0)] = 1
    return grid


def get_active_neighbors(grid, x, y, z, w):
    active = 0
    for dx in -1, 0, 1:
        for dy in -1, 0, 1:
            for dz in -1, 0, 1:
                dw_range = set((-1, 1, int(dx == 0 and dy == 0 and dz == 0)))
                for dw in dw_range:
                    active += grid.get((x + dx, y + dy, z + dz, w + dw), 0)
    return active


def get_boundaries(points):
    min_dim = lambda points, index: min(point[index] for point in points)
    max_dim = lambda points, index: max(point[index] for point in points)
    x_boundaries = min_dim(points, 0) - 1, max_dim(points, 0) + 1
    y_boundaries = min_dim(points, 1) - 1, max_dim(points, 1) + 1
    z_boundaries = min_dim(points, 2) - 1, max_dim(points, 2) + 1
    w_boundaries = min_dim(points, 3) - 1, max_dim(points, 3) + 1
    return x_boundaries, y_boundaries, z_boundaries, w_boundaries


def process_grid(grid):
    new_grid = {}
    x_range, y_range, z_range, w_range = get_boundaries(grid.keys())
    for x in range(x_range[0], x_range[1] + 1):
        for y in range(y_range[0], y_range[1] + 1):
            for z in range(z_range[0], z_range[1] + 1):
                for w in range(w_range[0], w_range[1] + 1):
                    active_neighbors = get_active_neighbors(grid, x, y, z, w)
                    if active_neighbors == 3 or grid.get((x, y, z, w), 0) and active_neighbors == 2:
                        new_grid[(x, y, z, w)] = 1
    return new_grid


def process(a):
    grid = parse_grid(a)
    for _iter in range(6):
        grid = process_grid(grid)
    return sum(grid.values())


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
