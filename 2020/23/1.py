class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def connect(self, node):
        self.next = node

    def get_value(self):
        return self.value


def read_file(fp):
    with open(fp, 'r') as ifs:
        for line in ifs:
            text = line.strip()
            if text:
                yield text


def get_previous_value(current, min_value, max_value, used):
    dec = lambda v, min_v, max_v: v - 1 if v > min_v else max_v

    x = dec(current, min_value, max_value)
    while x in used:
        x = dec(x, min_value, max_value)
    return x


def get_next_nodes(node, n):
    result = [node]
    while len(result) <= n:
        result.append(result[-1].next)
    return result[1:]


def process(a):
    nodes = {}
    first_value, *rest_values = map(int, list(a)[0])
    nodes[first_value] = head = prev = Node(first_value)
    for value in rest_values:
        nodes[value] = node = Node(value)
        prev.connect(node)
        prev = node
    prev.connect(head)

    all_values_sorted = sorted(nodes.keys())
    assert all(y - x == 1 for x, y in zip(all_values_sorted, all_values_sorted[1:])), f'Given values: {"".join(map(str, all_values_sorted))}'

    for _iter in range(100):
        nodes_to_reattach = get_next_nodes(head, 3)
        used = {node.get_value() for node in nodes_to_reattach}
        value_to_attach = get_previous_value(head.value, all_values_sorted[0], all_values_sorted[-1], used)
        node_to_attach = nodes[value_to_attach]

        head.connect(nodes_to_reattach[-1].next)
        nodes_to_reattach[-1].connect(node_to_attach.next)
        node_to_attach.connect(nodes_to_reattach[0])
        head = head.next

    while head.get_value() != 1:
        head = head.next

    result = []
    while head.get_value() not in result[:1]:
        result.append(head.get_value())
        head = head.next
    return ''.join(map(str, result[1:]))


if __name__ == '__main__':
    a = read_file('input.txt')
    r = process(a)
    print(r)
