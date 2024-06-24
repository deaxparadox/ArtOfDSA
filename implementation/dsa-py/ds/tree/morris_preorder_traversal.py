from typing import Self


# A binary tree Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Self = None
        self.right: Self = None
        

# Preorder traversal without
# recursion and without stack
def morris_traversal(root: Node):
    curr: Node = root
    
    while curr:
        # If left child is null, print the 
        # current node data, And, update
        # the current point to right child
        if curr.left is None:
            print(curr.data, end=" ")
            curr = curr.right
            
        else:
            # Find the inroder predecessor
            pre: Node = curr.left
            
            while pre.right is not None and pre.right is not curr:
                pre = pre.right
            
            # If the right child of inorder 
            # predecessor already points to 
            # the current node, update the
            # current with it's right child
            if pre.right is curr:
                pre.right = None
                curr = curr.right
                
            # else If right child doesn't point
            # to the current node, then print this
            # node's data and update the right child
            # pointer with the current node and update
            # the current with it's left child
            else:
                print(curr.data, end=" ")
                pre.right = curr
                curr = curr.left

# Function for Standard preorder traversal
def preorder(root: Node):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
        

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2) 
    root.right = Node(3) 
    
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    
    root.right.left= Node(6) 
    root.right.right = Node(7) 
    
    root.left.left.left = Node(8) 
    root.left.left.right = Node(9) 
    
    root.left.right.left = Node(10) 
    root.left.right.right = Node(11) 
    
    morris_traversal(root)
    print("\n")
    preorder(root)