from typing import Self, Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: Self = None
        self.right: Self = None
      
        
        
    def __lt__(self, other: Self) -> bool:
        return self.data < other.data
    
    def __le__(self, other: Self) -> bool:
        return self.data <= other.data
    
    
    def __gt__(self, other: Self) -> bool:
        return self.data > other.data
    
    def __ge__(self, other: Self) -> bool:
        return self.data >= other.data
    
    