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
        new_node->next = root;
        root = new_node;
    }
    return root;
}




Node * POPED = NULL;
/*
Remove the value from the list.
Return the new stack.
*/
Node * pop_first(Node * root) {

    // if root is empty
    if (!root)
        return NULL;

    Node * new_root = root;

    // for single node
    if (root->next == NULL) {
        POPED = root;
        new_root = NULL;
        return new_root;
    }


    
    POPED = root;
    new_root = root->next;

    return new_root;
}


/*
Print poped node
*/
void print_poped() {
    if (POPED == NULL) {
        printf("No item poped\n");
    } else {
        printf("Poped: %d\n", POPED->value);
        POPED = NULL;
    }
}

/*
Print the list;
*/
void print_list(Node * root) {
    while (root) {
        printf("%d -> ", root->value);
        root = root->next;
    }
    printf("\n");
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
    n = insert(n, 10);
    n = insert(n, 20);
    // insert(n, 49);
    // insert(n, 290);
    // insert(n, 123);
    // insert(n, 4534);
    // insert(n, 456);
    // insert(n, 89);
    
    // n = pop_first(n);
    // print_poped();

    
    // n = pop_first(n);
    // print_poped();

    print_list(n);


    free_list(n);
}