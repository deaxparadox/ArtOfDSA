from collections import namedtuple
from collections.abc import Collection
from abc import abstractmethod

class Graph:
    """
    Addes the vertex v to the graph
    Returns true if it wasn't already in the graph.
    """
    def addVertex(self, v) -> bool: ...
    
    """"
    Adds the edge e to the graph.
    Returns true if it wasn't already in the graph.
    """
    def addEdge(self, e) -> bool: ...
    
    """
    Retruns a Collection of all vertices in the graph.
    """
    def vertices(self) -> Collection: ...
    
    """
    Returns a collection of the edges that originates in vertex v.
    """
    def outGoingEdges(self, v: int)  -> Collection: ...
    
    """
    Returns the number of vertices in the graph.
    """
    def vertexCount(self) -> int: ...
    
    """
    Returns the number of edges in the graph.
    """
    def edgeCount(self) -> int: ...
    
Edge = namedtuple('Edge', ['start', 'end', 'weight'], defaults=[1.0])