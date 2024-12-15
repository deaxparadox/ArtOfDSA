#include <stdio.h>
#include <stdlib.h>


struct Node {
    int data;
    struct Node * left;
    struct Node * right;
};


struct Node * create_node(int data) {
    struct Node * temp = (struct node *) malloc(sizeof(struct Node));
    temp->left = NULL;
    temp->right = NULL;
    temp->data = data;
    return temp;
}




 