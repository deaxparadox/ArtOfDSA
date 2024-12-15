from collections import namedtuple
from collections.abc import Collection
from abc import abstractmethod

class Graph:
    def addVertex(self, v) -> bool: 
        """
        Addes the vertex v to the graph
        Returns true if it wasn't already in the graph.
        """
        ...
    
    
    
    def addEdge(self, e) -> bool: 
        """"
        Adds the edge e to the graph.
        Returns true if it wasn't already in the graph.
        """
        ...
    
    
    def vertices(self) -> Collection: 
        """
        Retruns a Collection of all vertices in the graph.
        """
        ...
    
    
    def outGoingEdges(self, v: int)  -> Collection: 
        """
        Returns a collection of the edges that originates in vertex v.
        """
        ...
    
    def vertexCount(self) -> int: 
        """
        Returns the number of vertices in the graph.
        """
        ...
    

    def edgeCount(self) -> int: 
        """
        Returns the number of edges in the graph.
        """
        ...
    
Edge = namedtuple('Edge', ['start', 'end', 'weight'], defaults=[1.0])