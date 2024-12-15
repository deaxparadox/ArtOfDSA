# Binary Search Algorithm

**Binary Search Algorithm** is a searching algorithm used in a **sorted array** by **repeatedly dividing the search internal in half**.

**Binary search** is used to find the position of the target value within a **sorted array**. It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty. The search interval is halved by comparing the target element with the middle value of the search space.

### Conditions to apply Binary Search Algorithm

- The data structure must be sorted.
- Access to any element of the data structure takes constant time.


### Working of Binary Search Algorithm

Consider an sorted array **arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}**, and the target **target = 23**.

**First Step**: Calculate the mid and compare the mid element with the key. If the key is less than mid element, move to left and if it is greater than the mid then move search space to the right.

- Key (i.e., 23) is greater than current mid element (i.e., 16). The search space moves to the right.

- Key is less than the current mid 56. The serach space moves to the left.

**Second Step**: If the key matches the value of the mid element, the element is found and stop search.

This process is repeated until we found the Key.


### Implementation types

The **Binary Search Algorithm** can be implemented in the following two ways:

- Iterative Binary Search Algorithm
- Recursive Binary Search Algorithm

### Recursive Binary Search Algorithm

- [Python implementation](../implementation/dsa-py/algorithms/binary_search.py)