import sys
from collections import deque
from iparser import read_input

def get_height(field, y, x):
    c = field[y][x]
    if c == 'E': c = 'z'
    if c == 'S': c = 'a'
    return ord(c)

def is_edge(field, curr_y, curr_x, next_y, next_x):
    if len(field) > next_y >= 0 <= next_x < len(field[next_y]):
        return get_height(field, next_y, next_x) - get_height(field, curr_y, curr_x) < 2
    return False

def process(data):
    field = list(data)
    start = end = None
    for i, r in enumerate(field):
        for j, c in enumerate(r):
            if c == 'S': start = i, j
            if c == 'E': end = i, j
    steps = 0
    q = deque([start])
    distance = {start: 0}
    while q:
        vertex = q.popleft()
        if vertex == end:
            return distance[vertex]
        y, x = vertex
        for dy, dx in zip([-1, 1, 0, 0], [0, 0, 1, -1]):
            if is_edge(field, y, x, y + dy, x + dx) and (y + dy, x + dx) not in distance:
                distance[(y + dy, x + dx)] = distance[vertex] + 1
                q.append((y + dy, x + dx))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
