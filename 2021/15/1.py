import sys
from heapq import heappop, heappush
from iparser import read_input

def process(graph):
    h, w = len(graph), len(graph[0])
    distance = {(0, 0): 0}
    queue = [(0, (0, 0))]
    while queue:
        local_distance, point = heappop(queue)
        if distance[point] < local_distance:
            continue
        x, y = point
        for dx, dy in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < w and 0 <= new_y < h:
                new_distance = local_distance + graph[new_y][new_x]
                if new_distance < distance.get((new_x, new_y), new_distance + 1):
                    distance[(new_x, new_y)] = new_distance
                    heappush(queue, (new_distance, (new_x, new_y)))
    return distance.get((w - 1, h - 1))

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
