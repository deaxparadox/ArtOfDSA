from typing import Any

from node import Node
from binary_tree import simple_tree
from height import height


def level_order(root: Node):
    """
    Function to level order traversal of tree
    """
    h = height(root)
    for i in range(1, h+1):
        current_level(root, i)
        
def current_level(root: Node, level: int):
    if root is None:
        return
    
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        current_level(root.left, level-1)
        current_level(root.right, level-1)

if __name__ == "__main__":
    b = simple_tree()
    
    level_order(b._root)