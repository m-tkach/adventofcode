import sys
from iparser import read_input

INFINITY = 1e18
ROOM_EXTENSION = ['DD', 'CB', 'BA', 'AC']

class Amphipod:
    TYPE_ENERGY = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000,
    }

    def __init__(self, amphipod_type):
        self.type = amphipod_type
        self.in_dest = False

    def mark_completed(self):
        self.in_dest = True

    def unmark_completed_DANGER(self):
        assert self.in_dest
        self.in_dest = False

    def is_completed(self):
        return self.in_dest

    def get_type(self):
        return self.type

    def get_room_index(self):
        for i, amphipod_type in enumerate(Amphipod.all_types()):
            if amphipod_type == self.type:
                return i
        return None

    def get_energy(self, distance):
        return Amphipod.TYPE_ENERGY.get(self.type) * distance

    @staticmethod
    def all_types():
        return Amphipod.TYPE_ENERGY.keys()

class Room:
    def __init__(self, dest_type, position, state):
        self.position = position
        self.type = dest_type
        self.size = len(state)
        self.amphipods = state[::-1]
        for amphipod in self.amphipods:
            if amphipod.get_type() == dest_type:
                amphipod.mark_completed()
            else:
                break

    def is_settled(self):
        for amphipod in self.amphipods:
            if amphipod.get_type() != self.type:
                return False
        return True

    def get_amphipod(self):
        if not self.amphipods:
            return None
        return self.amphipods[-1]

    def pop_amphipod(self, is_forced=False):
        if not self.amphipods:
            return None, None
        if not is_forced and self.get_amphipod().is_completed():
            return None, None
        amphipod = self.amphipods.pop()
        return amphipod, self.size - len(self.amphipods)

    def add_amphipod(self, amphipod, is_forced=False):
        if is_forced or self.can_add_amphipod(amphipod):
            self.amphipods.append(amphipod)
            return True, self.size - len(self.amphipods) + 1
        return False, None

    def can_add_amphipod(self, amphipod):
        if len(self.amphipods) == self.size:
            return False
        if amphipod.get_type() != self.type:
            return False
        return self.is_settled()

class Hallway:
    def __init__(self, length, rooms):
        self.positions = [None] * length
        for room in rooms:
            self.positions[room.position] = room

    def gen_actionable_items(self):
        for pos, item in enumerate(self.positions):
            if item is not None:
                yield item, pos

    def gen_empty_positions(self, room):
        room_index = room.position
        left, right = room_index - 1, room_index + 1
        while left >= 0 and not isinstance(self.positions[left], Amphipod):
            if self.positions[left] is None:
                yield left
            left -= 1
        while right < len(self.positions) and not isinstance(self.positions[right], Amphipod):
            if self.positions[right] is None:
                yield right
            right += 1

    def is_settled(self):
        for obj in self.positions:
            if obj is not None:
                if not isinstance(obj, Room):
                    return False
                if not obj.is_settled():
                    return False
        return True

    def is_locked(self):
        amphipods = []
        room_indices = []
        for i, item in enumerate(self.positions):
            if isinstance(item, Amphipod):
                amphipods.append((i, item.get_room_index()))
            elif isinstance(item, Room):
                room_indices.append(i)
        for i, (right_amphipod_index, right_room_i) in enumerate(amphipods):
            rigth_room_index = room_indices[right_room_i]
            for j, (left_amphipod_index, left_room_i) in enumerate(amphipods[:i]):
                left_room_index = room_indices[left_room_i]
                if rigth_room_index < left_amphipod_index and left_room_index > right_amphipod_index:
                    return True
        return False

    def move_between_rooms(self, src_room, dst_room):
        amphipod = src_room.get_amphipod()
        if not amphipod or amphipod.is_completed() or not dst_room.can_add_amphipod(amphipod):
            return False, None
        for pos in range(min(src_room.position, dst_room.position), max(src_room.position, dst_room.position) + 1):
            if isinstance(self.positions[pos], Amphipod):
                return False, None
        amphipod, in_src_room_movement = src_room.pop_amphipod()
        if amphipod is None:
            return False, None
        is_added, in_dst_room_movement = dst_room.add_amphipod(amphipod)
        assert is_added
        hallway_movement = abs(src_room.position - dst_room.position)
        amphipod.mark_completed()
        return True, amphipod.get_energy(in_src_room_movement + in_dst_room_movement + hallway_movement)

    def unmove_between_rooms_DANGER(self, src_room, dst_room):
        amphipod, _ = dst_room.pop_amphipod(is_forced=True)
        assert amphipod
        amphipod.unmark_completed_DANGER()
        is_added, _ = src_room.add_amphipod(amphipod, is_forced=True)
        assert is_added

    def move_from_room(self, room, dst_position):
        if self.positions[dst_position] is not None:
            return False, None
        for pos in range(min(room.position, dst_position), max(room.position, dst_position) + 1):
            item = self.positions[pos]
            if item is not None and not isinstance(item, Room):
                return False, None
        amphipod, in_room_movement = room.pop_amphipod()
        if amphipod is None:
            return False, None
        self.positions[dst_position] = amphipod
        hallway_movement = abs(room.position - dst_position)
        return True, amphipod.get_energy(in_room_movement + hallway_movement)

    def unmove_from_room_DANGER(self, room, dst_position):
        is_added, _ = room.add_amphipod(self.positions[dst_position], is_forced=True)
        assert is_added
        self.positions[dst_position] = None

    def move_to_room(self, src_position, room):
        amphipod = self.positions[src_position]
        if not isinstance(amphipod, Amphipod):
            return False, None
        for pos in range(min(room.position, src_position), max(room.position, src_position) + 1):
            if pos == src_position:
                continue
            item = self.positions[pos]
            if item is not None and not isinstance(item, Room):
                return False, None
        is_added, in_room_movement = room.add_amphipod(amphipod)
        if not is_added:
            return False, None
        hallway_movement = abs(room.position - src_position)
        self.positions[src_position] = None
        amphipod.mark_completed()
        return True, amphipod.get_energy(in_room_movement + hallway_movement)

    def unmove_to_room_DANGER(self, src_position, room):
        amphipod, _ = room.pop_amphipod(is_forced=True)
        assert isinstance(amphipod, Amphipod)
        self.positions[src_position] = amphipod
        amphipod.unmark_completed_DANGER()

    def print(self):
        n = len(self.positions) + 2
        print('#' * n)
        line = []
        room_len = 0
        for item in self.positions:
            if item is None:
                line.append('.')
            elif isinstance(item, Room):
                line.append('_')
                room_len = max(room_len, len(item.amphipods))
            else:
                line.append(ite,get_type())
        print('#' + ''.join(line) + '#')
        for i in range(room_len - 1, -1, -1):
            line = []
            for item in self.positions:
                if isinstance(item, Room):
                    line.append(item.amphipods[i].get_type() if i < len(item.amphipods) else ' ')
                else:
                    line.append('#')
            print('#' + ''.join(line) + '#')
        print('#' * n)

def go(hallway, rooms, energy, energy_limit):
    if hallway.is_settled():
        return energy
    result_energy = INFINITY
    if energy > energy_limit or hallway.is_locked():
        return result_energy
    actions = []
    for item, src_position in hallway.gen_actionable_items():
        if isinstance(item, Amphipod):
            room_index = item.get_room_index()
            room = rooms[room_index]
            is_moved, move_energy = hallway.move_to_room(src_position, room)
            if is_moved:
                actions.append((move_energy * 1e-4, hallway.move_to_room, hallway.unmove_to_room_DANGER, (src_position, room)))
                hallway.unmove_to_room_DANGER(src_position, room)
        elif isinstance(item, Room):
            amphipod = item.get_amphipod()
            if amphipod and not amphipod.is_completed():
                dst_room = rooms[amphipod.get_room_index()]
                is_moved, move_energy = hallway.move_between_rooms(item, rooms[amphipod.get_room_index()])
                if is_moved:
                    actions.append((0, hallway.move_between_rooms, hallway.unmove_between_rooms_DANGER, (item, rooms[amphipod.get_room_index()])))
                    hallway.unmove_between_rooms_DANGER(item, rooms[amphipod.get_room_index()])
                else:
                    for dst_position in hallway.gen_empty_positions(item):
                        is_moved, move_energy = hallway.move_from_room(item, dst_position)
                        if is_moved:
                            actions.append((move_energy, hallway.move_from_room, hallway.unmove_from_room_DANGER, (item, dst_position)))
                            hallway.unmove_from_room_DANGER(item, dst_position)
    for priority, apply_f, withdraw_f, args in sorted(actions, key=lambda i: i[0]):
        if priority >= result_energy:
            break
        is_moved, move_energy = apply_f(*args)
        assert is_moved
        total_energy = go(hallway, rooms, energy + move_energy, energy_limit)
        result_energy = min(total_energy, result_energy)
        withdraw_f(*args)
    return result_energy

def process(data):
    hallway_length, room_data, room_positions = data
    room_data = [
        room_line[:len(room_line) // 2] + [*room_ext] + room_line[len(room_line) // 2:]
        for room_line, room_ext in zip(room_data, ROOM_EXTENSION)
    ]
    amphipods, rooms = [], []
    for dest_type, room_position, room_amphipod_data in zip(Amphipod.all_types(), room_positions, room_data):
        room_amphipods = [Amphipod(amphipod_type) for amphipod_type in room_amphipod_data]
        rooms.append(Room(dest_type, room_position, room_amphipods))
        amphipods.extend(room_amphipods)
    hallway = Hallway(hallway_length, rooms)
    energy_limit = 100
    energy = INFINITY
    while energy == INFINITY:
        assert energy_limit < INFINITY
        print(f'Run for {energy_limit = }')
        energy = go(hallway, rooms, 0, energy_limit)
        energy_limit = int(energy_limit * 1.618) + 1
    return energy

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
