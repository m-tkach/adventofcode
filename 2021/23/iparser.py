import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    _, hallway_data, *room_data, _ = open(os.path.join(day_dir, filename), 'r')
    rooms = [[] for _ in [0] * 4]
    room_positions = [0] * 4
    for row in room_data:
        i = 0
        for j, c in enumerate(row):
            if c in 'ABCD':
                rooms[i].append(c)
                room_positions[i] = j - hallway_data.count('#') // 2
                i += 1
    return hallway_data.count('.'), rooms, room_positions
