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
    field, distance, q, end = [], {}, deque(), None
    for i, row in enumerate(data):
        field.append(row)
        for j, c in enumerate(row):
            if c in 'Sa':
                q.append((i, j))
                distance[(i, j)] = 0
            elif c == 'E':
                end = i, j
    while q:
        y, x = vertex = q.popleft()
        if vertex == end:
            return distance[vertex]
        for dy, dx in zip([-1, 1, 0, 0], [0, 0, 1, -1]):
            next_vertex = y + dy, x + dx
            if is_edge(field, y, x, *next_vertex) and next_vertex not in distance:
                distance[next_vertex] = distance[vertex] + 1
                q.append(next_vertex)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
