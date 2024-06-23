from .collection import Collection

class Set(Collection):
    def add(self, x):      """Adds x to the set. Returns true if the element wasn't already in the set."""
    def remove(self, x):   """Removes x from the set. Returns true if the element was in the set."""
    def contains(self, x): """Returns true if x is in the set."""
    # Note: __iter__() can yield the elements in any order.
    
    
class SortedSet(Set):
    def first(self):            """Returns the first (smallest) element. Raises an exception if the set is empty."""
    def last(self):             """Returns the last (largest) element. Raises an exception if the set is empty."""
    def floor(self, x):         """Returns the closest element <= x, or None if there is no such element."""
    def ceiling(self, x):       """Returns the closest element >= x, or None if there is no such element."""
    def lower(self, x):         """Returns the closest element < x, or None if there is no such element."""
    def higher(self, x):        """Returns the closest element > x, or None if there is no such element."""
    def between(self, x1, x2):  """Returns all elements x such that x1 <= x <= x2."""
    # Note: __iter__() should yield the elements in order.