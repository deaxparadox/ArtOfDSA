from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    @classmethod
    def mine(cls, root: Node):
        
        counter = -1
        # nodes = deque([root])
        nodes: list[Node] = [root]
        
        while True:
            
            # print(nodes)
            
            if len(nodes) == 0:
                break
            
            for _ in range(len(nodes)):
                    
                cur: Node = nodes.pop(0)
                
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
        
            counter+=1
            
        return counter

if __name__ == "__main__":
  
    # Representation of the input tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.left.left.left = Node(4)
    # root.left.left.right = Node(5)


    print(Solution.mine(root))