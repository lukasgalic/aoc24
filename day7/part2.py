class Node:
    def __init__(self, value=0, left=None, middle=None, right=None):
        self.value = value
        self.left = left
        self.middle = middle
        self.right = right


def eq_leaf_value(root, target_value):
    if root is None:
        return False
    if root.left is None and root.middle is None and root.right is None:
        return root.value == target_value
    return eq_leaf_value(root.left, target_value) or eq_leaf_value(root.middle, target_value) or eq_leaf_value(root.right, target_value)


def build_expression_tree(values):
    add_root = Node(values[0] + values[1])
    mul_root = Node(values[0] * values[1])
    c = int(str(values[0]) + str(values[1]))
    concat_root = Node(int(c))

    current_nodes = [add_root, concat_root, mul_root]

    # For each subsequent value, expand every node in current_nodes
    for x in values[2:]:
        next_nodes = []
        for node in current_nodes:
            # Create two children: one with addition, one with multiplication
            node.left = Node(node.value + x)
            node.middle = Node(int(str(node.value) + str(x)))
            node.right = Node(node.value * x)
            # Add these newly created nodes to next_nodes for further expansion
            next_nodes.extend([node.left, node.middle, node.right])
        current_nodes = next_nodes

    # Create a fake root that has both trees (from addition and multiplication) as children
    fake_root = Node(None, add_root, concat_root, mul_root)
    return fake_root


def equals_test_value(arr, test_value):
    lst = list(map(int, arr.split()))
    test_val = int(test_value)

    # Handle edge cases where input length is small
    if len(lst) == 2:
        c = int(str(lst[0]) + str(lst[1]))
        # Just check if either direct computation matches test_val
        return (lst[0] + lst[1] == test_val) or (lst[0] * lst[1] == test_val) or int(c) == test_val

    # Build a full expression tree exploring all add/mul combinations
    root = build_expression_tree(lst)

    # Check if any leaf equals the test_val
    return eq_leaf_value(root, test_val)


total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        test_value, arr = line.split(':')
        if equals_test_value(arr.strip(), test_value.strip()):
            total_sum += int(test_value)
print(total_sum)
