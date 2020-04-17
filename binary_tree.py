'''
given data = [0, 5, 7, 4, 3, 2, 20, 12, 6]

- create binary tree(from left to right, level by level)
- show the level order traversal of tree
- find the maximum number from left and right (max left + max right)

For example:

data [0, 5, 7, 4, 3, 2, 20, 12, 6]
tree structure:

           0
       /       \
       5        7
     /   \     /   \
    4     3   2    20
   / \
  12  6

level order traversal:
[
  [0],
  [5,7],
  [4, 3, 2, 20],
  [12, 6]
]

max number left and right (max left + max right)
sum([0, 5, 4, 12]) + sum([7, 20]) = 48
'''


class Node(object):
    left = None
    right = None

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "<Tree: {}>".format(self.value)

    @property
    def is_last(self):
        return True if not self.left and not self.right else False

    def get_max(self, find=None):
        nums = [self.value]
        current = self
        if find:
            current = getattr(self, find)
            nums.append(current.value)

        while not current.is_last:
            if current.left.value > current.right.value:
                nums.append(current.left.value)
                current = current.left
            else:
                nums.append(current.right.value)
                current = current.right
        return nums

    def get_sum_max(self):
        num = 0
        for direction in ["left", "right"]:
            num += sum(self.get_max(direction))

        return num

    @property
    def is_complete(self):
        return True if self.left and self.right else False


class Tree(object):
    root = None

    def add_node(self, node, num):
        if not node.left:
            node.left = Node(num)
            return node.left
        elif node.left and not node.right:
            node.right = Node(num)
            return node.right

    def next_node_ltr(self):
        '''
        find node, scan from top of the root (using ltr method)
        '''
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            if not node.is_complete:
                return node
            else:
                nodes.extend([node.left, node.right])

    def show_level_tree(self):
        tree_level = []
        nodes = [self.root]
        while nodes:
            next_nodes = []
            level_data = []

            for node in nodes:
                level_data.append(node.value)

                if node.left:
                    next_nodes.append(node.left)

                if node.right:
                    next_nodes.append(node.right)

            tree_level.append(level_data)
            nodes = next_nodes

        return tree_level

    def add(self, data):
        for num in data:
            if not self.root:
                self.root = Node(num)
                continue

            node = self.next_node_ltr()
            self.add_node(node, num)


data = [0, 5, 7, 4, 3, 2, 20, 12, 6]
tree = Tree()
tree.add(data)
print(tree.root.left.left.left)  # Tree (12)
print(tree.root.get_sum_max())  # 48
print(tree.show_level_tree())  # [[0], [5, 7], [4, 3, 2, 20], [12, 6]]
