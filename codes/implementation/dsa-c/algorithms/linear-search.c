#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool linear_search(int *arr, int *size, int *target) {
    for (int i=0; i<*size; i++) {
        printf("%d\t%d\n", *target, arr[i]);
        if (*target == arr[i]) {
            return true;
        }
    }
    return false;
}

int main() {
    int s = 10;
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target = 10;
    bool status = linear_search(arr, &s, &target);
    if (status == true) {
        printf("Target found\n");
    } else {
        printf("Target not found\n");
    }
    exit(0);
}