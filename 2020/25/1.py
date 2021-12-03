SUBJECT = 7
MOD = 20201227


def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def get_steps(public_key):
    candidate_key = 1
    step = 0
    while candidate_key != public_key:
        candidate_key = candidate_key * SUBJECT % MOD
        step += 1
    return step


def get_encryption_key(public_key, steps):
    encryption_key = 1
    for _iter in range(steps):
        encryption_key = encryption_key * public_key % MOD
    return encryption_key


def process(a):
    card_public, door_public = map(int, a)
    door_steps = get_steps(door_public)
    encryption_key = get_encryption_key(card_public, door_steps)
    assert encryption_key == get_encryption_key(door_public, get_steps(card_public))
    return encryption_key


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
