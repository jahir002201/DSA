class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.value, end=" ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root:
            print(root.value, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.value, end=" ")

tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("In-order Traversal:", end=" ")
tree.in_order_traversal(tree.root)
print("\nPre-order Traversal:", end=" ")
tree.pre_order_traversal(tree.root)
print("\nPost-order Traversal:", end=" ")
tree.post_order_traversal(tree.root)
