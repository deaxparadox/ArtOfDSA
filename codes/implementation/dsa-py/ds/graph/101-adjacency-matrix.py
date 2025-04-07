import typing

def add_edge(mat: list[list], i: int , j: int, /) -> None:
    # Add an edge between two vertices
    mat[i][j] = 1   # Graph is
    mat[j][i] = 1   # Undirected
    
def display_matrix(mat) -> None:
    
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))
        

# Main function to run the program
if __name__ == "__main__":
    
    # Number of vertices
    V = 4
    mat: list[list] = [[0] * V for _ in range(V)]
    
    # Add edges to the graph
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 2)
    add_edge(mat, 2, 3)
    
    # Optionally, initialize matrix directly
    """
    mat = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    """
    
    # Display adjacency matrix
    print("Adjacency Matrix: ")
    display_matrix(mat)