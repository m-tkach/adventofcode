import sys
from collections import defaultdict as dd
from iparser import read_input

def can_visit(v, seen, wildcard):
    if v.isupper():
        return True, wildcard
    if v != 'start' and seen == 1 and wildcard:
        return True, False
    return seen == 0, wildcard

def dfs(graph, v, used, wildcard):
    if v == 'end':
        return 1
    seen = used.get(v, 0)
    should_visit, wildcard = can_visit(v, seen, wildcard)
    if not should_visit:
        return 0
    pathes = 0
    used[v] = seen + 1
    for u in graph.get(v, []):
        pathes += dfs(graph, u, used, wildcard)
    used[v] -= 1
    return pathes

def process(data):
    graph = dd(list)
    add_edge = lambda u, v: graph[u].append(v)
    for u, v in data:
        add_edge(u, v)
        add_edge(v, u)
    return dfs(graph, 'start', dict(), True)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
