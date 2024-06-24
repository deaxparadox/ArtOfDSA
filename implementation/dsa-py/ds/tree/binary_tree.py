from typing import Self, Any

from node import Node


class BinaryTree:
    def __init__(self) -> None:
        self._root: Node = None
        
    def insert(self, data: Any):
        """
        Insert data in binary tree.
        """
        new_node: Node = Node(data)
        if not self._root:
            self._root = new_node
        else:
            self._insert(self._root, new_node)
            
    def _insert(self, root: Node, new_node: Node):
        if new_node < root:
            if root.left:
                self._insert(root.left, new_node)
            else:
                root.left = new_node
        else:
            if root.right:
                self._insert(root.right, new_node)
            else:
                root.right = new_node
        
        
def simple_tree() -> BinaryTree:
    b = BinaryTree()
    b.insert(1)
    b.insert(3)
    b.insert(2)
    b.insert(12)
    b.insert(20)
    return b