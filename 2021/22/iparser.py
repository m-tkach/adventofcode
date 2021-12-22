import os

class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                state, coordinates = text.split()
                coordinates = coordinates.split(',')
                coordinate_ranges = hashabledict()
                for c in coordinates:
                    dim = c[0]
                    left, right = map(int, c[2:].split('..'))
                    coordinate_ranges[dim] = (left, right)
                yield state, coordinate_ranges
