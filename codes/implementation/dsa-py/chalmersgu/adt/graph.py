class Graph:
    def addVertex(self, v):     """Adds the vertex v to the graph. Returns true if it wasn't already in the graph."""
    def addEdge(self, e):       """Adds the edge e to the graph. Returns true if it wasn't already in the graph."""
    def vertices(self):         """Returns a Collection of all vertices in the graph."""
    def outgoingEdges(self, v): """Returns a Collection of the edges that originates in vertex v."""
    def vertexCount(self):      """Returns the number of vertices in the graph."""
    def edgeCount(self):        """Returns the number of edges in the graph."""

from collections import namedtuple
Edge = namedtuple('Edge', ['start', 'end', 'weight'], defaults=[1.0])