import sys
from iparser import read_input

class Knot:
    def __init__(self, parent=None):
        self.parent = parent
        self.child = None
        if self.parent:
            self.parent._set_child(self)
        self.x = 0
        self.y = 0
        self.visited = set()
        self.__visit_point()

    def move(self, direction, distance):
        x_diff = (direction == 'R') - (direction == 'L')
        y_diff = (direction == 'D') - (direction == 'U')
        for _ in range(distance):
            self.x += x_diff
            self.y += y_diff
            self.__visit_point()
            if self.child:
                self.child._align_with_parent()

    def get_visited_points_count(self):
        return len(self.visited)

    def _set_child(self, child):
        self.child = child

    def _align_with_parent(self):
        if self.parent is None:
            return
        val_add = lambda v: (v < 0) - (v > 0)
        while self.__parent_distance() > 1:
            self.x, self.y = (t + val_add(t - h) for h, t in zip((self.parent.x, self.parent.y), (self.x, self.y)))
            self.__visit_point()
            if self.child:
                self.child._align_with_parent()

    def __parent_distance(self):
        if self.parent is None:
            return 0
        x_diff, y_diff = (h - t for h, t in zip((self.parent.x, self.parent.y), (self.x, self.y)))
        return max(abs(x_diff), abs(y_diff))

    def __visit_point(self):
        self.visited.add((self.x, self.y))

def process(data):
    root = tail = Knot()
    for _ in range(9):
        tail = Knot(tail)
    for direction, distance in data:
        root.move(direction, distance)
    return tail.get_visited_points_count()

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
