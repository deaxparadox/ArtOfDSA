# Linear or Sequential Search

This algorithm works by sequentially iterating through the whole array or list from one end until that target element is found. If the element is found, it returns its index, else -1.

Now let's look at an example and try to understand how it works:

```c
arr = {1, 12, 15, 11, 7, 19, 45};
```

Suppose the target element we want to search is  7.


### Approach for Linear or Sequential Search

- Start with index 0 and compare each element with the target
- If the target is found to be equal to the element, return its index
- If the target is not found, return -1