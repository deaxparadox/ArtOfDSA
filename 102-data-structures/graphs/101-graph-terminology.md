# Graph Terminology

### Undirected Graph

- **Adjacent Vertices**: As an edge *e* is represented by pair of vertices denoted by [*u*, *v*]. The vertices *u* and *v* are called endpoints of *e*. These vertices are also called adjacent vertices or neighbors.

- **Degree of a Vertices**: The degree of vertex *u*, written as *deg(u)*, is the number of edges containing *u*. If *deg(u)=0*, this means that vertex *u* doe snot belong to any edge, then vertex *u* is called an isolated vertex.

- **Path**: 
    - A *path* *P* of length *n* from a vertex *u* to vertex *v* is defined as sequence of (n+1) vertices, *i.e.*, *P = (v<sub>1</sub>, v<sub>2</sub>, v<sub>3</sub>,...v<sub>n+1</sub>)*, such that *u = v<sub>1</sub>*, *v = v<sub>n+1</sub>*, and *v<sub>i-1</sub>* is adjacent to *v<sub>i</sub>* for *i = 2, 3, ..., (n + 1)*.
    - The path is said to be *closed* i fthe endpoints of the path are same i.e. v<sub>1</sub> = v <sub>n+1</sub>.
    - The path is said to be *simple* if all the vertices in the sequence are distinct, with the exception that v<sub>1</sub> = v<sub>n+1</sub>. In that case it is known as *closed simple* path.

- **Cycle**: A *cycle* is a closed simple path with length 2 or more. Sometimes, a cycle of length *k* (i. e. *k* distinct vertices in the path) is known as *k-cycle*.