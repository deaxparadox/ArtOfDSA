from typing import Any, Self


class SingleNode:
    """
    Class `SingleNode` for single linked list.
    
    parameters:
    
    - data: value to store
    - nex: SingleNode next node
    """
    def __init__(self, data: Any | None = None, nex: Self | None = None) -> None:
        self.data: Any | None = data
        self.next: Self | None = nex
        
    '''
    Comparions functions
    '''
            
    def __eq__(self, other: Self):
        if not (isinstance(other, SingleNode)):
            raise TypeError("other must be a node.")
        return self.data == other.data
    
    def __lt__(self, other: Self):
        if not (isinstance(other, SingleNode)):
            raise TypeError("other must be a node.")
        return self.data < other.data
    
    def __gt__(self, other: Self):
        if not (isinstance(other, SingleNode)):
            raise TypeError("other must be a node.")
        return self.data > other.data

    


class DoubleNode:
    """
    Class `DoubleNode` for Double linked list.
    
    parameters:
    
    - data: value to store
    - nex: SingleNode next node
    """
    def __init__(self, data: Any | None = None, pre: Self | None = None, nex: Self | None = None) -> None:
        self.data: Any | None = data
        self.prev: Self | None = None
        self.next: Self | None = None
    

        