from node import Node
from binary_tree import BinaryTree

def height(root: Node):
    if not  root:
        return 0
    else:
        # compute the depth of each subtree
        l_height = height(root.left)
        r_height = height(root.right)
        
        # Use the larger one
        if (l_height > r_height):
            return l_height + 1
        else:
            return r_height + 1
        

if __name__ == "__main__":
    b = BinaryTree()
    b.insert(1)
    b.insert(3)
    b.insert(2)
    b.insert(12)
    b.insert(20)
    b.insert(21)
    b.insert(22)
    b.insert(23)
    print("Height: %s" % height(b._root))