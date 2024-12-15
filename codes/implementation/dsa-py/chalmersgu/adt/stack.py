from .collection import Collection

class Stack(Collection):
    def push(self, x): """Pushes x on top of the stack."""
    def pop(self):     """Pops the top of the stack and returns it. Raises an exception if the stack is empty."""
    def peek(self):    """Returns the top element, without removing it. Raises an exception if the stack is empty."""
    # Note: __iter__() should yield the elements starting from the top of the stack.