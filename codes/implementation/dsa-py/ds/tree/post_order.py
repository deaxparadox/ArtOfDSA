from node import Node
from binary_tree import BinaryTree

def postorder(root: Node):
    if (root):
        postorder(root.left)
        postorder(root.right)
        print("{}, ".format(root.data), end="")
        

if __name__ == "__main__":
    b = BinaryTree()
    b.insert(1)
    b.insert(3)
    b.insert(2)
    b.insert(12)
    b.insert(20)
    postorder(b._root)