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
append the value, and return pointer to last node.
*/
Node * append(Node * root, int value)
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




Node * POPED = NULL;
/*
Remove the value from the list.
Return the new stack.
*/
Node * pop(Node * root) {

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


    Node * pre = NULL;

    // iterate till last node
    while (root->next != NULL) {
        pre = root;
        root = root->next;
    }

    POPED = root;
    pre->next = NULL;

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
    append(n, 10);
    append(n, 20);
    // append(n, 49);
    // append(n, 290);
    // append(n, 123);
    // append(n, 4534);
    // append(n, 456);
    // append(n, 89);
    
    n = pop(n);
    print_poped();

    
    n = pop(n);
    print_poped();

    print_list(n);


    free_list(n);
}