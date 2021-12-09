import sys
from iparser import read_input

class Dsu:
    def __init__(self, n):
        self.parent = [*range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def comp_size(self, x):
        return self.size[self.find(x)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.comp_size(x) < self.comp_size(y):
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]

DELTA = [-1, 1, 0, 0]

def gen_neighbors(heatmap, x, y):
    for dx, dy in zip(DELTA, reversed(DELTA)):
        if 0 <= y + dy < len(heatmap) and 0 <= x + dx < len(heatmap[y]):
            yield y + dy, x + dx

def get_index(x, y, w):
    return x + y * w

def process(heatmap):
    h, w = len(heatmap), len(heatmap[0])
    dsu = Dsu(h * w)
    for y, row in enumerate(heatmap):
        for x, value in enumerate(row):
            if heatmap[y][x] == 9:
                continue
            for ny, nx in gen_neighbors(heatmap, x, y):
                if heatmap[ny][nx] == 9:
                    continue
                dsu.union(get_index(x, y, w), get_index(nx, ny, w))
    components = set()
    for y in range(h):
        for x in range(w):
            components.add(dsu.find(get_index(x, y, w)))
    component_sizes = sorted([dsu.comp_size(c) for c in components], reverse=True)
    result = 1
    for cs in component_sizes[:3]:
        result *= cs
    return result

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
