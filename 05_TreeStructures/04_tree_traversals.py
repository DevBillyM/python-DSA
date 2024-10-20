# Tree Traversals (In-order, Pre-order, Post-order)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

# Testing Tree Traversals
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)

print("In-order Traversal:", end=" ")
bt.inorder(bt.root)  # Output: 4 2 5 1 3

print("\nPre-order Traversal:", end=" ")
bt.preorder(bt.root)  # Output: 1 2 4 5 3

print("\nPost-order Traversal:", end=" ")
bt.postorder(bt.root)  # Output: 4 5 2 3 1
