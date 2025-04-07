# Hash Table (Hash Map)

A hash table, also known as hash map, is a data structure that maps keys to values. It is one part of a technique called hashing, the other of which is a hash function. A hash function is an algorithm that produces an index of where a value can be found or stored in hash table.

Some important notes about hash tables:

1. Values are not stored in sorted order.
2. You must account for potential collisions. This is usually done with a technique called chaining. Chaining means to create a linked list of values, the keys of which map to a certain index.

----------


Hashing is a technique in data structures that efficiently stores and retrieves data in a way that allows for quick access.

- Hashing involes mapping data to a specific index in a hash table (an array of items) using a **hash function**. It enables fast retrieval of information based on its key.
- The great thing about hashing is, we can achieve all three operations (search insert and delete) in O(1) time on average.
- Hashing is mainly used to implement a set of distinct items (only keys) and dictionaries (key values pairs).

[Hashing in Data Structure](/assets/Introduction-to-Hashing.webp)

----------

Hashing refers to the process of generating a small sized output (that can be used as index in a table) from an input of typically large and variable size. Hashing uses mathemtical formulas known as hash functions to do the transformation. This technique determines an index or location for the storage of an item in a data structure called Hash Table.

### Hash Table Data Structure Overview

- It is one of the most widely used data structures after arrays.
- It mainly supports search insert, and delete in O(1) time on average which is more efficient then other popular data structures like arrays, Linked List and Self Balancing BST.
- We use hashing of dictoinaries, frequency counting, maintaining data for quick access by key, etc.
- Real World Applications includes Database indexing, Cryptography, Caches, Symbol Tables and Dictionaries.
- There are mainly tow forms of hash typically implemented in programming languages.
    - **Hash Set**: Collection of unique keys.
    - **Hash Map**: Collection of key value pairs with keys being unique.

### Situations Where Hash is not Used 

- Need to maintain sorted data along with search, insert and delete. We use a self balancing BST in these cases.
- When Strings are keys and we need operations like prefix search along with search, insert and delete. We use Trie in these cases.
- When we need operations like floor and ceiling along with search, insert and/or delete. We use Self Balancing BST in these cases.

### Components of Hashing

There are majorly three components of hashing:

1. **Key**: A key can be anything string or integer which is fed as input in the hash function the technique that determines an index or location for storage of an item in a data structure.
2. **Hash Function**: Receives the input key and returns the index of an element in an array called hash table. The index is known as the hash index.
3. **Hash Table**: Hash table is typically an array of lists. It stores values corresponding to the keys. Hash stores the data in an associative manner in an array where each data value has its own unique index.

![Component of Hashing](/assets/Components-of-Hashing-1024.webp)

