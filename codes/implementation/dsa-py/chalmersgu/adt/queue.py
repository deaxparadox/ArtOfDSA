from .collection import Collection

class Queue(Collection):
    def enqueue(self, x): """Enqueues x at the end of the queue."""
    def dequeue(self):    """Dequeues the frontmost element. Raises an exception if the queue is empty."""
    def peek(self):       """Returns the frontmost element, without removing it. Raises an exception if the queue is empty."""
    # Note: __iter__() should yield the elements starting from the frontmost element.