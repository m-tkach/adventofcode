def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_line(s):
    return [c == '#' for c in s]


def process_grid(grid, x, y, dx, dy):
    total = 0
    while y < len(grid):
        total += grid[y][x % len(grid[y])]
        y += dy
        x += dx
    return total


def process(a):
    grid = list(map(parse_line, a))
    return process_grid(grid, 0, 0, 3, 1)



if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
