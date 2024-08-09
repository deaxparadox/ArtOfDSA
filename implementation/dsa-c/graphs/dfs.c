#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


// Structure for a node in adjancency list
struct Node {
    int data;
    struct Node * next;
};


// Structure for the adjancency list
struct List {
    struct Node * head;
};

// Structure for the graph
struct Graph
{
    int vertices;
    struct List * array;
};



// Function to create a new node 
struct Node * create_node(int data) {
    struct Node * new_node = (struct Node *) malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;

}


// Function to create a graph with a given number of vertices
struct Graph * create_graph(int vertices) 
{
    struct Graph * graph = (struct Graph *) malloc(sizeof(struct Graph));
    graph->vertices = vertices;
    graph->array = (struct List*)malloc(vertices * sizeof(struct List));
    
    for (int i=0; i<vertices; i++) {
        graph->array[i].head = NULL;
    }

    return graph;
}


// Function to add an edge to the graph
void add_edge(struct Graph * graph, int src, int dest)
{
    struct Node * new_node = create_node(dest);
    new_node->next = graph->array[src].head;
    graph->array[src].head = new_node;
}


// Function to perform Depth First Search (DFS) from a given vertex
void DFS(struct Graph * graph, int vertex, bool visited[])
{
    visited[vertex] = true;

    printf("%d ", vertex);

    struct Node * current_node = graph->array[vertex].head;

    while (current_node) {
        int adjacent_vertex = current_node->data;
        if (!visited[adjacent_vertex])
        {
            DFS(graph, adjacent_vertex, visited);
        }
        current_node = current_node->next;
    }
}


// Function to perform DFS traversal from a given vertex in a specified order
void DFSTraversal(struct Graph * graph, int * order, int order_size) {
    bool * visited = (bool *) malloc(graph->vertices * sizeof(bool));

    for (int i=0; i<graph->vertices; i++) {
        visited[i] = false;
    }

    for (int i=0; i<order_size; i++) {
        if (!visited[order[i]]) {
            DFS(graph, order[i], visited);
        }
    }

    free(visited);
}



int main()
{
    int vertices = 4;

    struct Graph * graph = create_graph(vertices);

    add_edge(graph, 2, 0);
    add_edge(graph, 0, 2);
    add_edge(graph, 1, 2);
    add_edge(graph, 0, 1);
    add_edge(graph, 3, 3);
    add_edge(graph, 1, 3);
 
    int order[] = {2, 0, 1, 3};
    int order_size = sizeof(order) / sizeof(order[0]);
 
    printf("Following is Depth First Traversal (starting from vertex 2):\n");
    DFSTraversal(graph, order, order_size);

    printf("\n");
 
    return 0;
}