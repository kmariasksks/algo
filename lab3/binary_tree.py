class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    stack = [tree]

    while stack:
        node = stack.pop(0)
        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return tree


def print_tree(tree):
    if tree is not None:
        print(tree.value)
        print_tree(tree.left)
        print_tree(tree.right)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Початковий вигляд:")
print_tree(root)

inverted_tree = invert_tree(root)

print("\nРезультат:")
print_tree(inverted_tree)
