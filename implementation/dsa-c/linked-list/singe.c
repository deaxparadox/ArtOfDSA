#include <stdio.h>
#include <stdlib.h>



// Node value storing data.
typedef struct __Node
{
    int value;
    struct __Node * next;
} Node;

/*
Create and return the node, created with value
*/
Node * create(int value) 
{
    Node * temp = (Node *) malloc(sizeof(Node));
    temp->value = value;
    temp->next = NULL;
    return temp;
} 


/*
Insert the value, and return pointer to last node.
*/
Node * insert(Node * root, int value)
{
    Node * new_node = create(value);
    if (!root) {
        // if root is NULL
        return new_node;
    } else {
        // If root is not NULL
        while (root->next != NULL) {
            root = root->next;
        }
        root->next = new_node;
    }
    return new_node;
}

/*
Print the list;
*/
void print_list(Node * root) {
    while (root) {
        printf("%d -> ", root->value);
        root = root->next;
    }
}

/*
Free the list;
*/
void free_list(Node * root) {
    Node * temp = NULL;
    while (root) {
        temp = root;
        root = root->next;
        free(temp);
    }
}

int main()
{
    
    Node * n = create(1923);
    insert(n, 10);
    insert(n, 20);
    insert(n, 49);
    insert(n, 290);
    print_list(n);
    free_list(n);
}