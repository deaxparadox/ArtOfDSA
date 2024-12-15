from collections.abc import Collection
from graph_api import Graph, Edge


class MatrixGraph(Graph):
    _edgeMatrix: list[list[float]]
    _totalEdges: int
    
    def __init__(self, numVertices: int) -> None:
        self._edgeMatrix = [[0] * numVertices for _ in range(numVertices)]
        self._totalEdges = 0
        
    def vertexCount(self) -> int:
        return self._totalEdges
    
    def addVertex(self, v: int) -> bool:
        raise NotImplementedError("You cannot add vertices  to a MatrixGraph")
    
    def addEdge(self, e: Edge[int]) -> bool:
        if e.weight == 0:
            raise ValueError("Edges cannot have weight 0")
        isNew: bool = self._edgeMatrix[e.start][e.end] == 0
        if isNew:
            self._totalEdges += 1
        return isNew
    
    def vertices(self) -> Collection:
        return range(self.vertexCount())
    
    def outGoingEdges(self, v: int) -> Collection:
        outgoing = [
            Edge(v, w, weight) 
            for (w, weight) in enumerate(self._edgeMatrix[v])
            if weight != 0
        ]
        return outgoing
    
    # For an adjacency matrix, it's much more efficient to get information
    # about known edges, then to search through outgoingEdges,
    # so we add these two as convenience methods.
    
    def isEdge(self, v: int, w: int) -> bool:
        return self._edgeMatrix[v][w] != 0
    
    def edgeWegith(self, v: int, w: int) -> float:
        return self._edgeMatrix[v][w]