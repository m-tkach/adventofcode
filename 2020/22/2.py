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


def check_and_extend(used, players):
    queue_strs = map(lambda queue: '|'.join(map(str, queue)), players)
    super_queue_str = ':'.join(queue_strs)
    status = super_queue_str in used
    used.add(super_queue_str)
    return status


def game(players):
    used = set()
    last_winner = None
    step = 0
    while all(players):
        if check_and_extend(used, players):
            return 0
        moves = [(players[i].pop(0), i) for i in range(len(players))]
        if all(card <= len(players[i]) for card, i in moves):
            new_decks = [player[:card] for (card, _), player in zip(moves, players)]
            last_winner = game(new_decks)
        else:
            last_winner = max(moves)[1]
        players[last_winner].extend([card for card, _ in sorted(moves, key=lambda item: item[1] == last_winner, reverse=True)])
    return last_winner


def process(a):
    players = parse_input(a)
    winner = game(players)
    return sum(card * (i + 1) for i, card in enumerate(players[winner][::-1]))


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
