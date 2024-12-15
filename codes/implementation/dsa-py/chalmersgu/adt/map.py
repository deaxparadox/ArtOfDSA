from .iterable import Iterable


class Map(Iterable):
    def put(self, key, value):  """Sets the value of the given key. Returns the previous value, or None."""
    def get(self, key):         """Returns the value associated with the given key, or None if the key is not there."""
    def remove(self, key):      """Removes and returns the value associated with the given key, or None if there is no key."""
    def containsKey(self, key): """Returns true if the key has an associated value."""
    def isEmpty(self):          """Returns true if there are no keys."""
    def size(self):             """Returns the number of keys (i.e., the number of key/value pairs)."""
    # Note: __iter__() can yield the keys in any order.
    
    
class SortedMap(Map):
    def firstKey(self):                """Returns the first (smallest) key. Raises an exception if the map is empty."""
    def lastKey(self):                 """Returns the last (largest) key. Raises an exception if the map is empty."""
    def floorKey(self, key):           """Returns the closest key <= k, or None if there is no key."""
    def ceilingKey(self, key):         """Returns the closest key >= k, or None if there is no key."""
    def lowerKey(self, key):           """Returns the closest key < k, or None if there is no such element."""
    def higherKey(self, key):          """Returns the closest key > k, or None if there is no such element."""
    def keysBetween(self, key1, key2): """Returns all keys k such that k1 <= k <= k2."""
    # Note: __iter__() should yield the keys in order.