import sys
from iparser import read_input

class Queue:
    def __init__(self):
        self.clear()

    def empty(self):
        return self.front >= len(self.data)

    def push(self, x):
        self.data.append(x)

    def pop(self):
        self.front += 1
        return self.data[self.front - 1]

    def processed(self):
        return self.front

    def clear(self):
        self.data = []
        self.front = 0

def process(data):
    h, w = len(data), len(data[0])
    q = Queue()
    step = 0
    while q.processed() != h * w:
        step += 1
        q.clear()
        for i in range(h):
            for j in range(w):
                data[i][j] += 1
                if data[i][j] == 10:
                    q.push((i, j))
        while not q.empty():
            i, j = q.pop()
            for di in -1, 0, 1:
                for dj in -1, 0, 1:
                    if not di == 0 == dj and 0 <= i + di < h and 0 <= j + dj < w:
                        data[i + di][j + dj] += 1
                        if data[i + di][j + dj] == 10:
                            q.push((i + di, j + dj))
        for i in range(h):
            for j in range(w):
                if data[i][j] > 9:
                    data[i][j] = 0
    return step

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
