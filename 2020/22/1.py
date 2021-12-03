def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def parse_input(a):
    players = [[], []]
    player = None
    for line in a:
        if 'Player' in line:
            player = int(line.split()[1][:-1]) - 1
        else:
            players[player].append(int(line))
    return players


def process(a):
    players = parse_input(a)
    assert len(players) == 2
    card_ids = [0] * len(players)
    last_winner = None
    while all(front < len(queue) for front, queue in zip(card_ids, players)):
        move = []
        for i in range(len(players)):
            front = card_ids[i]
            card_ids[i] += 1
            card = players[i][front]
            move.append((card, i))
        move.sort(reverse=True)
        last_winner = move[0][1]
        for card, _ in move:
            players[last_winner].append(card)
    front = card_ids[last_winner]
    return sum(card * (i + 1) for i, card in enumerate(players[last_winner][front:][::-1]))


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
