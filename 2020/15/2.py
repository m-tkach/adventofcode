def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


class State:
    def __init__(self, values):
        self.positions = {}
        self.prev, *items = values
        self.index = 1
        for v in items:
            self.positions[self.prev] = self.index
            self.prev = v
            self.index += 1

    def getNext(self):
        prev_index = self.positions.get(self.prev, self.index)
        self.positions[self.prev] = self.index
        self.prev = self.index - prev_index
        self.index += 1
        return self.prev

    def getIndex(self):
        return self.index


def process_single(a):
    state = State(map(int, a.split(',')))
    k = len(a)
    while state.getIndex() < 30000000:
        v = state.getNext()
        if (state.getIndex() % 500000) == 0:
            print(state.getIndex())
    return v


def process(a):
    return [process_single(x) for x in a]


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(*r)
