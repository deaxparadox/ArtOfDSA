# Working of LRU Cache

Let's suppose we have an LRU cache of **capacity 3**, and we would like to perform the following operations:

- **put (key=1, value=A)** into the cache
- **put (key=2, value=B)** into the cache
- **put (key=3, value=C)** into the cache
- **get (key=2)** from the cache
- **get (key=4)** from the cache
- **put (key=4, value=D)** into the cache
- **put (key=3, value=E)** into the cache
- **get (key=4)** from the cache
- **put (key=1, value=A)** into the cache

The above operations are performed one after another as shown in the image below:

[Image no found](/assets/lru-cache-1.png)

### Detailed Explanation of each operation

1. **put (key=1, value=A)**: Since LRU cache has empty capacity=3, there is no need for any replacement and we put {1: A} at the top i.e. {1:A} has highest priority.
2. **put (key=2, value=B)**: Since LRU cache has empty capacity=2, again there is no need for any replacement, but now the {2:B} has the highest priority and priority of {1:A} decrease.
3. **put (key=3, value=C)**: Still there is 1 empty space vacant in the cache, therefor put {3:C} without any replacement, notice now the cache is full and the current order of priority from highest to lowest is {3:C}, {2:B}, {1:A}.
4. **get (key=2)**: Now, return value of key=2 during the operation, also since key=2 is used, now the new priority order is {2:B}, {3:C}, {1:A}.
5. **get (key=4)**: Observe that key 4 is not present in the cache, we return ‘-1’ for this operation.
6. **put (key=4, value=D)** : Observe that cache is FULL, now use LRU algorithm to determine which key is least recently used. Since {1:A} had the least priority, remove {1:A} from our cache and put {4:D} into the cache. Notice that the new priority order is {4:D}, {2:B}, {3:C}
7. **put (key=3, value=E)** : Since key=3 was already present in the cache having value=C, so this operation won’t result in removal of any key, rather it will update the value of key=3 to ‘ E’ . Now, the new order of priority will become {3:E}, {4:D}, {2:B}
8. **get (key=4)** : Return the value of key=4. Now, new priority will become {4:D}, {3:E}, {2:B}
9. **put (key=1, value=A)** : Since our cache is FULL, so use our LRU algorithm to determine which key was least recently used, and since {2:B} had the least priority, remove {2:B} from our cache and put {1:A} into the cache. Now, the new priority order is {1:A}, {4:D}, {3:E}.