from node import Node
from binary_tree import BinaryTree

def preorder(root: Node):
    if (root):
        print("{}, ".format(root.data), end="")
        preorder(root.left)
        preorder(root.right)
        

if __name__ == "__main__":
    b = BinaryTree()
    b.insert(1)
    b.insert(3)
    b.insert(2)
    b.insert(12)
    b.insert(20)
    preorder(b._root)