import sys
from collections import defaultdict as dd
from iparser import read_input

def mark(used, v):
    if v.islower():
        used.add(v)

def unmark(used, v):
    if v.islower():
        used.remove(v)

def dfs(graph, v, used):
    if v == 'end':
        return 1
    if v.islower() and v in used:
        return 0
    pathes = 0
    mark(used, v)
    for u in graph.get(v, []):
        pathes += dfs(graph, u, used)
    unmark(used, v)
    return pathes

def process(data):
    graph = dd(list)
    add_edge = lambda u, v: graph[u].append(v)
    for u, v in data:
        add_edge(u, v)
        add_edge(v, u)
    return dfs(graph, 'start', set())

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
