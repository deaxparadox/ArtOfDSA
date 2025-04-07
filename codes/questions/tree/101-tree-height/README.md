# Height of Binary Tree

Given a **binary tree**, the task is to find the **maximum height** of the tree. The height of the tree is the **number of edges** in the tree from the root to the deepest node.

Examples:

The height of the bolow binary tree is 2.

![Image not found](/assets/tree-1.png)

*If you calculate the **edges** is the longest path, it will be 2, while the number of nodes in 3*. Therefore, Total number of edges in a path will always to 1 less than total number of nodes.

### Codes

#### Approach 1: Using Recursion - O(n) Time and O(h) Space

<!-- Uses DFS Algorithm. -->

The idea is to recusively calculate the **height** of the **left** and **right** subtress of a node and assign height to the node as **max** of the heights of the two children plus 1.

- [Python](height-recursion.py)

**Time complexity**: O(n), where **n** is the number of nodes in the binary tree, as each nodes in the binary tree, as each node is visited once.
**Auxiliary Space**: O(h) where **h** is height of the binary tree.

#### Approach 2: Using level order traversal - O(n) Time and O(h) Space

The idea is, if we take a closer look at the DFS, we can notice that after we process the **last node** of the current level, the next level is completely in the **queue**. We use this property and insert a special **NULL** into the queue to indicate end of a level.

- [Python](height-level-order.py)