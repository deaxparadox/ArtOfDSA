#include <stdio.h>
#include <stdlib.h>

#define LIMIT 10

int linear_search(int numbers[], int target) {
    for (int i=0; i<LIMIT; i++) {
        printf("%d\n", numbers[i]);
        if (numbers[i] = target) {
            return i;
        }
    }
    return -1;
}

int main() {
    int numbers[LIMIT];

    for (int i=0; i<LIMIT; i++) {
        numbers[i] = i+10;;
    }

    int target = 1500;
    int index = linear_search(numbers, target);
    if (index < 0) {
        printf("Number doesn't exist in Arrays.\n");
    } else {
        printf("\nFound\nIndex of %d is %d\n", target, index);
    }
    
    exit(0);
}