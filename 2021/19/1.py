import sys
from collections import deque, defaultdict as dd
from itertools import permutations
from iparser import read_input

MATCHES_LIMIT = 12
DIMENSIONS = 3

class Beacon:
    def __init__(self, position):
        self.coordinates = position

    def get_transformed_coordinates(self, signs, permutation):
        assert all(c in [-1, 1] for c in signs)
        assert {*permutation} == {*range(len(self.coordinates))}
        return [signs[p] * self.coordinates[p] for p in permutation]

    def apply_transformation(self, signs, permutation):
        self.coordinates = self.get_transformed_coordinates(signs, permutation)

    def get_difference(self, other, transformation=None):
        if transformation is None:
            return [a - b for a, b in zip(self.coordinates, other.coordinates)]
        signs, permutation = transformation
        return [a - b for a, b in zip(self.coordinates, other.get_transformed_coordinates(signs, permutation))]

    def apply_move(self, diff_coordinates):
        self.coordinates = [c + d for c, d in zip(self.coordinates, diff_coordinates)]

class Scanner:
    def __init__(self):
        self.beacons = []

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

    def compare(self, other):
        for transformation in Scanner.gen_transformations():
            dist_diff = dd(int)
            matches = 0
            for self_beacon in self.beacons:
                for other_beacon in other.beacons:
                    diff_coordinates = tuple(self_beacon.get_difference(other_beacon, transformation))
                    dist_diff[diff_coordinates] += 1
                    if dist_diff[diff_coordinates] >= MATCHES_LIMIT:
                        return True, (transformation, diff_coordinates)
        return False, None

    def apply_transformation(self, signs, permutation):
        for beacon in self.beacons:
            beacon.apply_transformation(signs, permutation)

    def apply_move(self, diff_coordinates):
        for beacon in self.beacons:
            beacon.apply_move(diff_coordinates)

    def merge(self, other):
        self_beacons_data = [tuple(b.coordinates) for b in self.beacons]
        other_beacons_data = [tuple(b.coordinates) for b in other.beacons]
        self.beacons = [Beacon(list(beacon_data)) for beacon_data in {*self_beacons_data, *other_beacons_data}]

    @staticmethod
    def gen_transformations():
        for p in permutations(range(DIMENSIONS)):
            for x_sign in -1, 1:
                for y_sign in -1, 1:
                    for z_sign in -1, 1:
                        yield [x_sign, y_sign, z_sign], p

def process(data):
    scanners = []
    for scanner_data in data:
        new_scanner = Scanner()
        for beacon_data in scanner_data:
            new_scanner.add_beacon(Beacon(beacon_data))
        scanners.append(new_scanner)
    main_scanner = scanners[-1]
    queue = deque(range(len(scanners) - 1))
    while queue:
        scanner_id = queue.popleft()
        scanner = scanners[scanner_id]
        status, extras = main_scanner.compare(scanner)
        if status:
            transformation, fixed_diff_coordinates = extras
            scanner.apply_transformation(*transformation)
            scanner.apply_move(fixed_diff_coordinates)
            main_scanner.merge(scanner)
        else:
            queue.append(scanner_id)
    global_beacons_coordinates = set()
    for beacon in main_scanner.beacons:
        global_beacons_coordinates.add(tuple(beacon.coordinates))
    return len(global_beacons_coordinates)

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
