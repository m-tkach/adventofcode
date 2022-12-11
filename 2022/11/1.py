import sys
from iparser import read_input

ROUNDS = 20

class Monkey:
    def __init__(self, monkey_id, items, inspect_operation, div_test):
        self.id = monkey_id
        self.items = items
        self.operation = inspect_operation
        self.div_test = div_test
        self.next_monkeys = []
        self.__is_fully_initialised = False
        self.inspected_items_count = 0

    def init_next_monkeys(self, true_monkey, false_monkey):
        self.next_monkeys = [false_monkey, true_monkey]
        self.__is_fully_initialised = True

    def inspect_items(self):
        assert self.__is_fully_initialised, 'You need to call self.init_next_monkeys(...) first'
        while self.items:
            item = self.operation(self.items.pop()) // 3
            self.next_monkeys[item % self.div_test == 0].receive_item(item)
            self.inspected_items_count += 1

    def receive_item(self, item):
        self.items.append(item)

    def get_inspected_items_count(self):
        return self.inspected_items_count

def process(data):
    monkeys = {}
    for monkey_id, items, operation, div_test, *_ in data:
        monkeys[monkey_id] = Monkey(monkey_id, items, operation, div_test)
    for monkey_id, *_, true_monkey_id, false_monkey_id in data:
        monkeys[monkey_id].init_next_monkeys(monkeys[true_monkey_id], monkeys[false_monkey_id])
    for _ in range(ROUNDS):
        for monkey in monkeys.values():
            monkey.inspect_items()
    result = 1
    for x in sorted(map(Monkey.get_inspected_items_count, monkeys.values()))[-2:]:
        result *= x
    return result

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
