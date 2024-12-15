from node import Node
from binary_tree import BinaryTree

def inorder(root: Node):
    if (root):
        inorder(root.left)
        print("{}, ".format(root.data), end="")
        inorder(root.right)
        

if __name__ == "__main__":
    b = BinaryTree()
    b.insert(1)
    b.insert(3)
    b.insert(2)
    b.insert(12)
    b.insert(20)
    inorder(b._root)