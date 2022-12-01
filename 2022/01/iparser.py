import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        elf = []
        for line in ifs:
            cal = line.strip()
            if cal:
                elf.append(int(cal))
            else:
                if elf:
                    yield elf
                elf = []
