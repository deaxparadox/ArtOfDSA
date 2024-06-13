from collections.abc import Collection
from graph_api import Graph, Edge

class MatrixGraph(Graph):
    _edgeMatrix: list[list[float]]
    _totalEdges: int
    
    def __init__(self, numVertices: int):
        self._edgeMatrix = [[0] * numVertices for _ in range(numVertices)]
        self._totalEdges = 0
        
    def vertexCount(self) -> int:
        return len(self._edgeMatrix)
    
    def addVertex(self, v) -> bool:
        raise NotImplementedError("You cannot add vertices to a MatrixGraph")
    
    def addEdge(self, e: Edge[int]) -> bool:
        if e.weight == 0:
            raise ValueError("Edges cannot have weight 0")
        isNew: bool = self._edgeMatrix[e.start][e.end] == 0
        self._edgeMatrix[e.start][e.end] = e.weight
        if isNew:
            self._totalEdges +=1
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
    
    
    def isEdge(self, v: int, w: int) -> bool:
        return self._edgeMatrix[v][w] != 0
    
    def edgeWeight(self, v: int, w: int) -> float:
        return self._edgeMatrix[v][w]