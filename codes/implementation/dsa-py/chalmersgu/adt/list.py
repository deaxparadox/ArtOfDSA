from .collection import Collection

class List(Collection):
    def add(self, i, x): """Adds x at position i; where 0 <= i <= size."""
    def get(self, i):    """Returns the element at position i; where 0 <= i < size."""
    def set(self, i, x): """Replaces the value at position i with x; where 0 <= i < size."""
    def remove(self, i): """Removes the element at position i; where 0 <= i < size."""
    # Note: __iter__() should yield the elements starting from position 0.