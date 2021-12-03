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
        if self.prev not in self.positions:
            self.positions[self.prev] = self.index
            self.prev = 0
            self.index += 1
        else:
            prev_index = self.positions.get(self.prev)
            self.positions[self.prev] = self.index
            self.prev = self.index - prev_index
            self.index += 1
        return self.prev

    def getIndex(self):
        return self.index


def process_single(a):
    state = State(map(int, a.split(',')))
    k = len(a)
    while state.getIndex() < 2020:
        v = state.getNext()
    return v


def process(a):
    return [process_single(x) for x in a]


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(*r)
