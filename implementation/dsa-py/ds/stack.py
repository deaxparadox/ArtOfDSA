from typing import Any, Self

from node import SingleNode



class Stack:
    def __init__(self, data: Any | None = None) -> None:
        self.__length = 0
        self.head: SingleNode | None = None
        
        if data:
            self.push(data)
        
    def push(self, data: Any | None = None) -> Self:
        """
        Push to stack
        """
        n: SingleNode = SingleNode(data, self.head)
        self.head = n
        self.__length +=1
        return self.head
    
    def __len__(self) -> int:
        """
        Return the length of stack
        """
        return self.__length
    
    
    def print(self):
        """
        Print stack
        """
        while self.head:
            print(self.head.data)
            self.head = self.head.next
    


if __name__ == "__main__":
    s = Stack(1)
    s.push(2)
    s.push(3)
    s.print()