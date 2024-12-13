class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def eq_leaf_value(root, target_value):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.value == target_value
    return eq_leaf_value(root.left, target_value) or eq_leaf_value(root.right, target_value)


def build_expression_tree(values):
    add_root = Node(values[0] + values[1])
    mul_root = Node(values[0] * values[1])

    current_nodes = [add_root, mul_root]

    for x in values[2:]:
        next_nodes = []
        for node in current_nodes:

            node.left = Node(node.value + x)
            node.right = Node(node.value * x)

            next_nodes.extend([node.left, node.right])
        current_nodes = next_nodes

    fake_root = Node(None, add_root, mul_root)
    return fake_root


def equals_test_value(arr, test_value):
    lst = list(map(int, arr.split()))
    test_val = int(test_value)

    if len(lst) == 2:

        return (lst[0] + lst[1] == test_val) or (lst[0] * lst[1] == test_val)

    root = build_expression_tree(lst)

    return eq_leaf_value(root, test_val)


total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        test_value, arr = line.split(':')
        if equals_test_value(arr.strip(), test_value.strip()):
            total_sum += int(test_value)
print(total_sum)
