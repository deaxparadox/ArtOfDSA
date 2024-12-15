from .collection import Collection

class PriorityQueue(Collection):
    def add(self, x):    """Adds x to the priority queue."""
    def removeMin(self): """Removes and returns the minimum element. Raises an exception if the priority queue is empty."""
    def getMin(self):    """Returns the minimum element, without removing it. Raises an exception if the priority queue is empty."""
    # Note: __iter__() can yield the elements in any order, but the minimum element should come first.