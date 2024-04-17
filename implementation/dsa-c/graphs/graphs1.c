#include <stdio.h>
#include <stdlib.h>

#define MAX 50

typedef struct nodeType1
{
    int vertex;
    struct nodeType1 *next;
} gnode1;




// CREATING AN EMPTY GRAPH
void createGraph(gnode1 *adj[], int num);

// INPUT GRAPH
void inputGraph(gnode1 *adj[], int num); 


// OUTPUTTING A GRAPH
void printGraph(gnode1 *adj[], int num);

// DELETING A GRAPH
void deleteGraph(gnode1 *adj[], int n);

int main() {
    gnode1 *adj[MAX];
    int n;
    printf("\nEnter number of nodes in the graph: ");
    scanf("%d", &n);
    createGraph(adj, n);
    inputGraph(adj, n);
    // clrscr();
    printf("\n INPUT GRAPH \n\n");
    printGraph(adj, n);
    printf("\nPress any key to continue...");
    getchar();
    deleteGraph(adj, n);
}

void createGraph(gnode1 *adj[], int num)
{
    int i;
    for (i=1; i<=num; i++) {
        adj[i] = NULL;
    }
}

void inputGraph(gnode1 *adj[], int num)
{
    gnode1 *ptr, *last;
    int i, j, m, val, wt;
    for (i=0; i<=num; i++)
    {
        last = NULL;
        printf("\nNUmber of nodes in the adjacency list of node %d ", i);
        scanf("%d", &m);
        for (j=1; j<=m; j++) 
        {
            printf("Enter node #%d: ", j);
            scanf("%d", &val);
            ptr = (gnode1 *) malloc(sizeof(gnode1));
            ptr->vertex = val;
            ptr->next = NULL;

            if (adj[i] == NULL) 
                adj[i] = last = ptr;
            else
            {
                last->next = ptr;
                last = ptr;
            }
        }
    }
}

void printGraph(gnode1 *adj[], int num) {
    gnode1 *ptr;
    int i;
    for (i=1; i<=num; i++) {
        ptr = adj[i];
        printf(" %d", i);
        while (ptr != NULL) {
            printf("-> %d", ptr->vertex);
            ptr = ptr->next;
        }
        printf("\n");
    }
}


void deleteGraph(gnode1 *adj[], int n)
{
    int i=0;
    gnode1 *temp, *ptr;
    for (i=0; i<=n; i++) {
        ptr = adj[i];
        while (ptr!=NULL) {
            temp = ptr;
            ptr = ptr->next;
            free(temp);
        }
        adj[i] = NULL;
    }

}