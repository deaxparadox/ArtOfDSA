# Note: by implementing these methods,
# one can loop over the elements in a standard Python for-loop.
class Iterator:
    def __iter__(self): """Returns the iterator itself."""
    def __next__(self): """Returns the next item. Raises StopIteration if there are no more elements."""

