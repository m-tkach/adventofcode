import os

def read_input(filename):
    day_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(day_dir, filename), 'r') as ifs:
        records = []
        for line in ifs:
            text = line.strip()
            if text:
                records.append(eval(text))
        records = iter(records)
        return zip(records, records)
