import sys
from iparser import read_input

class Node:
    def __init__(
        self,
        level=0,
        value=None,
        left_child=None,
        right_child=None,
    ):
        self.level = level
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.left_sibling = None
        self.right_sibling = None

    def should_explode(self):
        if self.left_child and self.right_child and self.level > 4:
            return self.left_child.value is not None and self.right_child.value is not None
        return False

    def explode(self):
        if self.should_explode():
            left_child, right_child = self.left_child, self.right_child
            self.left_sibling = self.left_child.left_sibling
            if self.left_sibling:
                self.left_sibling.value += self.left_child.value
                self.left_sibling.right_sibling = self
            self.right_sibling = self.right_child.right_sibling
            if self.right_sibling:
                self.right_sibling.value += self.right_child.value
                self.right_sibling.left_sibling = self
            self.value = 0
            self.left_child = None
            self.right_child = None
            return True
        return False

    def should_split(self):
        return self.value is not None and self.value > 9

    def split(self):
        if self.should_split():
            self.left_child = Node(level=self.level + 1, value=self.value // 2)
            if self.left_sibling:
                self.left_child.left_sibling = self.left_sibling
                self.left_sibling.right_sibling = self.left_child
                self.left_sibling = self.left_child
            self.right_child = Node(level=self.level + 1, value=-(-self.value // 2))
            if self.right_sibling:
                self.right_child.right_sibling = self.right_sibling
                self.right_sibling.left_sibling = self.right_child
                self.right_sibling = self.right_child
            self.value = None
            self.left_child.right_sibling = self.right_child
            self.right_child.left_sibling = self.left_child
            return True
        return False

class Tree:
    def __init__(self, data):
        self._create_tree(data)

    def _create_tree(self, data):
        def __create_tree(data, level=1):
            if type(data) == int:
                return Node(level=level, value=data)
            left, right = data
            return Node(
                level=level,
                left_child=__create_tree(left, level + 1),
                right_child=__create_tree(right, level + 1)
            )

        def __update_left_sibling(node, sibling=None):
            if not node:
                return sibling
            if node.value is not None:
                node.left_sibling = sibling
                return node
            sibling = __update_left_sibling(node.left_child, sibling)
            return __update_left_sibling(node.right_child, sibling)

        def __update_right_sibling(node, sibling=None):
            if not node:
                return sibling
            if node.value is not None:
                node.right_sibling = sibling
                return node
            sibling = __update_right_sibling(node.right_child, sibling)
            return __update_right_sibling(node.left_child, sibling)

        self.root = __create_tree(data)
        __update_left_sibling(self.root)
        __update_right_sibling(self.root)

    def merge(self, o):
        def inc_level(node):
            if node:
                node.level += 1
                inc_level(node.left_child)
                inc_level(node.right_child)

        def get_leftmost_node(node):
            if not node:
                return None
            return get_leftmost_node(node.left_child) or node

        def get_rightmost_node(node):
            if not node:
                return None
            return get_rightmost_node(node.right_child) or node

        inc_level(self.root)
        inc_level(o.root)
        rightmost = get_rightmost_node(self.root)
        leftmost = get_leftmost_node(o.root)
        rightmost.right_sibling = leftmost
        leftmost.left_sibling = rightmost
        self.root = Node(level=1, left_child=self.root, right_child=o.root)

    def reduce(self):
        def dfs_explode(node):
            if node:
                return dfs_explode(node.left_child) + node.explode() + dfs_explode(node.right_child)
            return False
        def dfs_split(node):
            if node:
                return dfs_split(node.left_child) or node.split() or dfs_split(node.right_child)
            return False

        while dfs_explode(self.root) or dfs_split(self.root):
            ...

class SnailfishNumber:
    def __init__(self, data=None):
        self.tree = data and Tree(data)

    def add(self, o):
        if not self.tree:
            self.tree = o.tree
        else:
            self.tree.merge(o.tree)
        self.tree.reduce()

    def magnitude(self):
        def dfs(node):
            if node.value is not None:
                return node.value
            return 3 * dfs(node.left_child) + 2 * dfs(node.right_child)
        return dfs(self.tree.root)

def process(data):
    data = list(data)
    mg = 0
    for i, x in enumerate(data):
        for j, y in enumerate(data):
            if i != j:
                snailfish = SnailfishNumber(x)
                snailfish.add(SnailfishNumber(y))
                mg = max(mg, snailfish.magnitude())
    return mg

if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
