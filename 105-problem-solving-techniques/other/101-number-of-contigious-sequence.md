### To determine the number of contigious sequence

Imagine having an array of 10 integers, and we need for to find the all the contigious sequence (the number sequence in the array which are continous).

The following function will return, the number of contigious sequence in Python.


```py
def main(arr: int, k: int):
    return len(arr) - k + 1
```

Usage:

We have array `arr` with values `[1, 23, 12, 54, 23, 5, 3, 8]`. To find the find the number contigious sub-sequence, we need to call the *main* function with argument *arr: array length* and *k: size of sub sequence*.

```py
In [8]: arr = [1, 3, 4, 5, 6, 23, 12, 43]

In [9]: alen = len(arr)

In [10]: def arr_sub_seq(arr: int, k: int):
    ...:     return arr - k + 1
    ...: 

In [12]: arr_sub_seq(alen, 5)
Out[12]: 4

```

If you manually calculate the *sub-sequence* of size '5' in 'arr' from above example code, you will output '4'.
