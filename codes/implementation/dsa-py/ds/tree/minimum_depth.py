from binary_tree import simple_tree
from node import Node

from typing import Optional
from collections import deque

def min_depth_recursion(root: Optional[Node]):
    # Corner case. Should never be hit unless
    # the code is called on root = None
    if root is None:
        return 0
    
    # Base case: Leaf node.
    # This accoutns for height = 1
    if root.left is None and root.right is None:
        return 1
    
    # If left subtree is None, 
    # recur for right subtree
    if root.left is None:
        return min_depth_recursion(root.right) + 1
    
    # If right subtree is None,
    # recur for left subtree
    if root.right is None:
        return min_depth_recursion(root.left) + 1
    
    return min(min_depth_recursion(root.left), min_depth_recursion(root.right))+1



def min_depth_loop(root: Optional[Node]) -> int:
    level = 0
    if root is None:
        return level
    else:
        level+=1

    outer = deque()
    outer.append(root)
    leaf = True
    while leaf:
        inner = deque()
        while outer:
            n = outer.popleft()
            if not n.left and not n.right:
                leaf = False
                break
            if n.left:
                inner.append(n.left)
            if n.right:
                inner.append(n.right)
            level+=1
        outer = inner
    return level

if __name__ == "__main__":
    s = simple_tree()
    
    print(min_depth_loop(s._root))
    print(min_depth_recursion(s._root))