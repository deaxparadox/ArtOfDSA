# TOC (Basic to Advanced)

*Built from CLRS 4th ed. (incl. its new online algorithms, matching and ML chapters), ACM/IEEE/AAAI CS2023 Algorithmic Foundations units (Foundational DS and Algorithms, Strategies, Complexity, Models), and Oxford's advanced algorithms syllabus (amortised analysis, union-find, red-black and splay trees, max flow, linear programming, approximation and exponential algorithms).*

---

## PART 0: PREREQUISITES

**Ch 0. Prerequisites**

- 0.1 Computational thinking: abstraction, decomposition, pattern recognition
- 0.2 Pseudocode and flowcharts
- 0.3 Variables, data types, operators, control flow, functions, scope
- 0.4 How memory works: stack vs heap, addresses, pointers/references, value vs reference semantics
- 0.5 Number representation: binary, two's complement, overflow, floating-point precision
- 0.6 Basic discrete math: sets, functions, relations, logic, proofs (direct, contradiction, induction)
- 0.7 Counting: permutations, combinations, pigeonhole, inclusion-exclusion
- 0.8 Logarithms, exponents, floor/ceil, modular arithmetic
- 0.9 Summations and series (arithmetic, geometric, harmonic)
- 0.10 Basic probability and expected value

---

## PART I: FOUNDATIONS OF ALGORITHMS

**Ch 1. The Role of Algorithms in Computing**

- 1.1 What an algorithm is; properties (finiteness, definiteness, input, output, effectiveness)
- 1.2 Data structure vs abstract data type (ADT) vs implementation
- 1.3 Algorithms as a technology; why efficiency matters
- 1.4 Problem types: decision, search, optimization, counting

**Ch 2. Getting Started: Analysing and Designing**

- 2.1 Insertion sort as a first algorithm
- 2.2 Loop invariants (initialization, maintenance, termination)
- 2.3 Correctness proofs, pre/post-conditions
- 2.4 Models of computation: RAM model, word size, cost model

**Ch 3. Characterising Running Time**

- 3.1 Best, worst, average case
- 3.2 Asymptotic notation: O, Ω, Θ, o, ω
- 3.3 Common growth rates (1, log n, √n, n, n log n, n², n³, 2ⁿ, n!)
- 3.4 Time vs space complexity; auxiliary vs total space
- 3.5 Analysing loops, nested loops, conditionals, function calls
- 3.6 Standard notations and common functions

**Ch 4. Recursion**

- 4.1 Base case, recursive case, call stack
- 4.2 Tracing recursion trees
- 4.3 Recurrence relations: substitution, recursion-tree, master theorem, Akra-Bazzi
- 4.4 Tail recursion and conversion between recursion and iteration
- 4.5 Space cost of recursion; stack overflow
- 4.6 Classic recursive problems (factorial, Fibonacci, GCD, power, Tower of Hanoi, subsets, permutations)

**Ch 5. Problem-Solving Methodology**

- 5.1 Understanding constraints and edge cases
- 5.2 Brute force → optimization
- 5.3 Testing: unit tests, edge cases, stress testing
- 5.4 Reading constraints to infer the target complexity

---

## PART II: LINEAR DATA STRUCTURES

**Ch 6. Arrays**

- 6.1 Static arrays: memory layout, indexing, bounds
- 6.2 Dynamic arrays: resizing and amortised cost
- 6.3 Insertion, deletion, search, traversal costs
- 6.4 Multi-dimensional arrays: row-major vs column-major
- 6.5 Sparse arrays and matrices
- 6.6 Circular arrays, rotation, reversal, in-place techniques
- 6.7 Array problems: max subarray (Kadane), merging, partitioning, Dutch national flag

**Ch 7. Strings**

- 7.1 Representation: character encodings (ASCII, Unicode, UTF-8), mutability, immutability
- 7.2 Basic operations: concatenation, substring, comparison, reversal
- 7.3 Palindromes, anagrams, frequency counting
- 7.4 String builders and buffers

**Ch 8. Linked Lists**

- 8.1 Singly, doubly and circular linked lists
- 8.2 Sentinel/dummy nodes
- 8.3 Insert, delete, search, reverse, merge
- 8.4 Cycle detection (Floyd), finding middle, nth from end
- 8.5 Arrays vs linked lists trade-offs
- 8.6 Unrolled linked lists, XOR linked lists, skip lists (intro)

**Ch 9. Stacks**

- 9.1 LIFO ADT; array and linked implementations
- 9.2 Expression evaluation: infix, prefix, postfix, conversion
- 9.3 Balanced parentheses, undo/redo, call-stack simulation
- 9.4 Monotonic stack
- 9.5 Min-stack and stack with auxiliary data

**Ch 10. Queues and Deques**

- 10.1 FIFO ADT; array, circular and linked implementations
- 10.2 Deque (double-ended queue)
- 10.3 Priority queue (ADT intro)
- 10.4 Queue using stacks and stack using queues
- 10.5 Monotonic deque
- 10.6 Uses: scheduling, buffering, BFS

**Ch 11. Hashing**

- 11.1 Hash functions: division, multiplication, universal hashing
- 11.2 Collision resolution: chaining, open addressing (linear, quadratic, double hashing), Robin Hood, cuckoo, hopscotch
- 11.3 Load factor and rehashing
- 11.4 Hash maps, hash sets, multisets
- 11.5 Hashing patterns: frequency maps, two-sum, grouping, deduplication
- 11.6 Perfect hashing
- 11.7 Rolling hash
- 11.8 Cryptographic vs non-cryptographic hashes (overview)

**Ch 12. Other Abstract Data Types**

- 12.1 Dictionary/map, set, multiset/bag
- 12.2 Ordered map and ordered set
- 12.3 List ADT, sequence ADT
- 12.4 Bitset/bit array
- 12.5 Choosing a data structure for a problem

---

## PART III: SEARCHING AND SORTING

**Ch 13. Searching**

- 13.1 Linear/sequential search, sentinel search
- 13.2 Binary search: iterative, recursive, boundary variants (lower/upper bound)
- 13.3 Binary search on answer / on monotonic functions
- 13.4 Ternary search, exponential search, interpolation search, jump search
- 13.5 Searching rotated and 2D sorted arrays

**Ch 14. Elementary Sorting**

- 14.1 Sorting concepts: stability, in-place, adaptivity, comparison vs non-comparison, internal vs external
- 14.2 Bubble, selection, insertion sort
- 14.3 Shell sort

**Ch 15. Efficient Sorting**

- 15.1 Merge sort (top-down, bottom-up), counting inversions
- 15.2 Quicksort: partition schemes (Lomuto, Hoare), pivot selection, randomized quicksort, 3-way quicksort
- 15.3 Heapsort
- 15.4 Introsort and hybrid sorts (Timsort idea)
- 15.5 Lower bound for comparison sorting (Ω(n log n))

**Ch 16. Linear-Time Sorting**

- 16.1 Counting sort
- 16.2 Radix sort
- 16.3 Bucket sort

**Ch 17. Selection and Order Statistics**

- 17.1 Min/max and simultaneous min-max
- 17.2 Quickselect (randomized selection)
- 17.3 Median of medians (worst-case linear selection)
- 17.4 k-th largest/smallest, top-k problems

**Ch 18. External and Special Sorting**

- 18.1 External merge sort
- 18.2 Sorting networks
- 18.3 Parallel sorting (overview)
- 18.4 Topological ordering as a sort (cross-ref Part VI)

---

## PART IV: TREES

**Ch 19. Tree Fundamentals**

- 19.1 Terminology: root, leaf, height, depth, level, degree, subtree
- 19.2 Representations: pointer-based, array-based, parent array, left-child/right-sibling
- 19.3 General (n-ary) trees
- 19.4 Binary trees: full, complete, perfect, balanced, degenerate

**Ch 20. Tree Traversals**

- 20.1 Pre-order, in-order, post-order (recursive and iterative)
- 20.2 Level-order (BFS)
- 20.3 Morris traversal
- 20.4 Reconstructing a tree from traversals
- 20.5 Serialization/deserialization

**Ch 21. Binary Search Trees**

- 21.1 BST property; search, insert, delete
- 21.2 Successor, predecessor, min, max
- 21.3 Validation, LCA in BST, range queries, k-th smallest
- 21.4 Degeneration and need for balancing

**Ch 22. Balanced Search Trees**

- 22.1 AVL trees and rotations
- 22.2 Red-black trees
- 22.3 Splay trees
- 22.4 Treaps and randomized BSTs
- 22.5 Scapegoat trees, weight-balanced trees
- 22.6 2-3 trees, 2-3-4 trees, left-leaning red-black trees
- 22.7 AA trees
- 22.8 Order-statistic trees and interval trees (augmented trees)

**Ch 23. Heaps and Priority Queues**

- 23.1 Binary heap (min/max): array representation, sift-up/down
- 23.2 Build-heap in O(n)
- 23.3 Heap operations: insert, extract, decrease-key, delete
- 23.4 d-ary heaps
- 23.5 Binomial heaps, Fibonacci heaps, pairing heaps, leftist heaps, skew heaps
- 23.6 Indexed priority queues
- 23.7 Median maintenance (two heaps), top-k, k-way merge

**Ch 24. Tries (Prefix Trees)**

- 24.1 Standard trie, compressed trie (radix/Patricia), ternary search tree
- 24.2 Prefix search, autocomplete, longest common prefix
- 24.3 Binary/XOR trie
- 24.4 Suffix trie (intro)

**Ch 25. Disjoint Set Union (Union-Find)**

- 25.1 Make-set, find, union
- 25.2 Union by rank/size, path compression/halving
- 25.3 Inverse Ackermann analysis
- 25.4 Applications: connected components, Kruskal, cycle detection
- 25.5 DSU with rollback, weighted DSU, offline DSU

**Ch 26. Range-Query Structures**

- 26.1 Prefix sums and difference arrays (1D and 2D)
- 26.2 Sparse table (RMQ)
- 26.3 Segment tree: point/range update, range query
- 26.4 Lazy propagation
- 26.5 Fenwick tree / Binary Indexed Tree (1D, 2D)
- 26.6 Merge sort tree, wavelet tree, persistent segment tree
- 26.7 Sqrt decomposition and Mo's algorithm
- 26.8 Segment tree beats, dynamic and implicit segment trees

**Ch 27. Disk-Based and Multi-Way Trees**

- 27.1 B-trees, B+ trees, B*-trees
- 27.2 External-memory data structures
- 27.3 LSM trees (overview)
- 27.4 Cache-oblivious structures (van Emde Boas layout)

---

## PART V: GRAPHS

**Ch 28. Graph Fundamentals**

- 28.1 Terminology: vertex, edge, directed/undirected, weighted, degree, path, cycle, connectivity
- 28.2 Special graphs: DAG, tree, bipartite, complete, planar, sparse/dense, multigraph
- 28.3 Representations: adjacency matrix, adjacency list, edge list, incidence matrix
- 28.4 Implicit graphs (grids, state spaces)

**Ch 29. Graph Traversal**

- 29.1 Breadth-first search
- 29.2 Depth-first search; discovery/finish times; edge classification
- 29.3 Connected components, flood fill
- 29.4 Bipartite check, cycle detection (directed and undirected)
- 29.5 Topological sort (Kahn, DFS-based)
- 29.6 0-1 BFS, multi-source BFS, bidirectional BFS
- 29.7 Iterative deepening DFS

**Ch 30. Shortest Paths**

- 30.1 Optimal substructure and relaxation
- 30.2 Dijkstra (array, binary heap, Fibonacci heap)
- 30.3 Bellman-Ford and negative cycles
- 30.4 SPFA
- 30.5 DAG shortest paths
- 30.6 Floyd-Warshall, transitive closure
- 30.7 Johnson's algorithm
- 30.8 A* and heuristics; bidirectional Dijkstra
- 30.9 Difference constraints

**Ch 31. Minimum Spanning Trees**

- 31.1 Cut and cycle properties
- 31.2 Kruskal, Prim
- 31.3 Borůvka
- 31.4 Second-best MST, MST variants
- 31.5 Directed MST (Chu-Liu/Edmonds)

**Ch 32. Connectivity**

- 32.1 Strongly connected components (Kosaraju, Tarjan)
- 32.2 Articulation points and bridges
- 32.3 Biconnected components
- 32.4 2-SAT
- 32.5 Eulerian paths/circuits; Hamiltonian paths (overview)

**Ch 33. Trees as Graphs**

- 33.1 Tree diameter, center, rerooting
- 33.2 Lowest common ancestor: binary lifting, Euler tour + RMQ, Tarjan offline
- 33.3 Heavy-light decomposition
- 33.4 Centroid decomposition
- 33.5 Euler tour flattening
- 33.6 Tree DP, tree isomorphism, virtual trees, link-cut trees

**Ch 34. Network Flow and Matching**

- 34.1 Flow networks, residual graphs, max-flow min-cut
- 34.2 Ford-Fulkerson, Edmonds-Karp, Dinic, push-relabel
- 34.3 Min-cost max-flow
- 34.4 Bipartite matching: Hopcroft-Karp, König's theorem
- 34.5 Hungarian algorithm (assignment problem)
- 34.6 Stable matching (Gale-Shapley)
- 34.7 General graph matching (Blossom)
- 34.8 Circulations with demands, flow applications

**Ch 35. Advanced Graph Topics**

- 35.1 Graph coloring
- 35.2 Cliques, independent sets, vertex cover
- 35.3 Planar graphs
- 35.4 Dominator trees
- 35.5 Dynamic graph algorithms
- 35.6 Spectral methods (PageRank basics)
- 35.7 Graph isomorphism (overview)

---

## PART VI: ALGORITHM DESIGN PARADIGMS

**Ch 36. Brute Force and Exhaustive Search**

- 36.1 Generating subsets, permutations, combinations
- 36.2 Pruning and search-space estimation

**Ch 37. Divide and Conquer**

- 37.1 Paradigm and recurrences
- 37.2 Merge sort, quicksort, binary search as D&C
- 37.3 Strassen's matrix multiplication
- 37.4 Closest pair of points
- 37.5 Karatsuba multiplication
- 37.6 Maximum subarray, counting inversions
- 37.7 FFT as D&C
- 37.8 D&C optimization (for DP)

**Ch 38. Greedy Algorithms**

- 38.1 Greedy-choice property and exchange argument
- 38.2 Activity/interval scheduling, interval partitioning
- 38.3 Fractional knapsack
- 38.4 Huffman coding
- 38.5 Job sequencing, scheduling to minimize lateness
- 38.6 Minimum platforms, meeting rooms
- 38.7 Matroids and greedy
- 38.8 Greedy on graphs (Prim, Kruskal, Dijkstra)
- 38.9 When greedy fails

**Ch 39. Backtracking**

- 39.1 State-space tree, choose-explore-unchoose
- 39.2 Pruning and constraint propagation
- 39.3 N-Queens, Sudoku, subset sum, word search, permutations with duplicates
- 39.4 Graph coloring, Hamiltonian cycle
- 39.5 Branch and bound

**Ch 40. Dynamic Programming**

- 40.1 Overlapping subproblems, optimal substructure
- 40.2 Memoization (top-down) vs tabulation (bottom-up)
- 40.3 State design, transitions, base cases, ordering
- 40.4 Space optimization (rolling arrays)
- 40.5 Reconstructing solutions
- 40.6 1D DP: Fibonacci, climbing stairs, house robber, coin change, LIS
- 40.7 2D DP: grid paths, LCS, edit distance, matrix-chain multiplication
- 40.8 Knapsack family: 0/1, unbounded, bounded, subset sum, partition
- 40.9 String DP: palindromic substrings, regex/wildcard matching
- 40.10 Interval DP; optimal BST
- 40.11 Bitmask DP; TSP
- 40.12 Digit DP
- 40.13 Tree DP; DP on DAGs
- 40.14 Probability and expected-value DP
- 40.15 Optimizations: convex hull trick, Knuth, divide-and-conquer optimization, SOS DP, matrix-exponentiation DP
- 40.16 Profile (broken-profile) DP

**Ch 41. Randomized Algorithms**

- 41.1 Las Vegas vs Monte Carlo
- 41.2 Probabilistic analysis and indicator random variables
- 41.3 Randomized quicksort/select
- 41.4 Reservoir sampling, shuffling (Fisher-Yates)
- 41.5 Karger's min-cut
- 41.6 Miller-Rabin primality
- 41.7 Hashing-based randomization, fingerprinting (Freivalds)

**Ch 42. Incremental, Sweep and Other Techniques**

- 42.1 Incremental construction
- 42.2 Sweep-line technique
- 42.3 Meet in the middle
- 42.4 Reduction and transformation
- 42.5 Amortized design
- 42.6 Parametric search

---

## PART VII: PROBLEM-SOLVING PATTERNS

**Ch 43. Core Patterns**

- 43.1 Two pointers
- 43.2 Sliding window (fixed and variable)
- 43.3 Prefix sum / hashing patterns
- 43.4 Fast and slow pointers
- 43.5 Merge intervals, sweep over intervals
- 43.6 Cyclic sort
- 43.7 In-place linked-list reversal
- 43.8 Monotonic stack/queue patterns
- 43.9 Top-K elements, K-way merge
- 43.10 Subsets/permutations/combinations patterns
- 43.11 Binary search on answer
- 43.12 Topological-sort patterns
- 43.13 Union-find patterns
- 43.14 Matrix/grid traversal patterns

**Ch 44. Bit Manipulation**

- 44.1 Bitwise operators, shifts, masks
- 44.2 Set/clear/toggle/check bit; counting set bits; power-of-two checks
- 44.3 XOR tricks, single-number problems
- 44.4 Subset enumeration with bitmasks, Gray code
- 44.5 Bit-parallel algorithms

---

## PART VIII: STRING ALGORITHMS

**Ch 45. Pattern Matching**

- 45.1 Naive matching
- 45.2 Rabin-Karp
- 45.3 Knuth-Morris-Pratt, prefix function/failure function
- 45.4 Z-algorithm
- 45.5 Boyer-Moore, Horspool, Sunday
- 45.6 Finite automaton matching
- 45.7 Bitap (shift-and), approximate matching

**Ch 46. Advanced String Structures**

- 46.1 Suffix array and LCP array
- 46.2 Suffix tree (Ukkonen)
- 46.3 Suffix automaton
- 46.4 Aho-Corasick (multi-pattern matching)
- 46.5 Manacher's algorithm
- 46.6 Palindromic tree (Eertree)
- 46.7 Burrows-Wheeler transform, FM-index

**Ch 47. String Problems**

- 47.1 Longest common substring/subsequence
- 47.2 Edit distance variants
- 47.3 Lyndon words, minimal rotation, string periodicity
- 47.4 Sequence alignment (Needleman-Wunsch, Smith-Waterman)
- 47.5 Regular expression matching engines

**Ch 48. Compression and Coding**

- 48.1 Run-length encoding
- 48.2 Huffman, arithmetic coding
- 48.3 LZ77/LZ78/LZW
- 48.4 Error-detecting/correcting codes (parity, Hamming, CRC)

---

## PART IX: MATHEMATICAL AND NUMERICAL ALGORITHMS

**Ch 49. Number Theory**

- 49.1 GCD (Euclid), extended Euclid, LCM
- 49.2 Modular arithmetic, modular inverse, fast exponentiation
- 49.3 Primality testing; sieve of Eratosthenes, segmented sieve, linear sieve
- 49.4 Prime factorization, Pollard's rho
- 49.5 Euler's totient, Fermat's little theorem, Euler's theorem
- 49.6 Chinese Remainder Theorem
- 49.7 Discrete logarithm, primitive roots
- 49.8 Combinatorics with modulus: nCr, Catalan, Lucas theorem
- 49.9 RSA (overview)

**Ch 50. Matrices and Linear Algebra**

- 50.1 Matrix multiplication; Strassen
- 50.2 Matrix exponentiation (Fibonacci, linear recurrences)
- 50.3 Gaussian elimination, LU decomposition, determinant
- 50.4 Solving linear systems; matrix inversion

**Ch 51. Polynomials and FFT**

- 51.1 Polynomial representations; evaluation, interpolation
- 51.2 Fast Fourier Transform
- 51.3 Number-theoretic transform
- 51.4 Fast multiplication; convolution applications

**Ch 52. Linear Programming**

- 52.1 Standard and slack forms
- 52.2 Simplex algorithm
- 52.3 Duality
- 52.4 Integer programming (overview)

**Ch 53. Computational Geometry**

- 53.1 Points, vectors, cross/dot product, orientation
- 53.2 Line segment intersection (sweep line)
- 53.3 Convex hull: Graham scan, Jarvis march, Andrew's monotone chain
- 53.4 Closest pair of points
- 53.5 Polygon area, point in polygon
- 53.6 Rotating calipers
- 53.7 Half-plane intersection
- 53.8 Voronoi diagrams, Delaunay triangulation
- 53.9 Spatial structures: k-d tree, quadtree, octree, R-tree, BSP tree

**Ch 54. Game Theory and Combinatorial Games**

- 54.1 Minimax, alpha-beta pruning
- 54.2 Nim, Sprague-Grundy theorem
- 54.3 Game DP

**Ch 55. Numerical Methods**

- 55.1 Floating-point issues
- 55.2 Newton's method, bisection
- 55.3 Numerical integration (overview)
- 55.4 Optimization: gradient descent, ternary search

---

## PART X: ADVANCED DATA STRUCTURES

**Ch 56. Probabilistic and Approximate Structures**

- 56.1 Bloom filter, counting Bloom filter, cuckoo filter
- 56.2 Count-Min Sketch
- 56.3 HyperLogLog
- 56.4 MinHash, locality-sensitive hashing
- 56.5 Skip lists

**Ch 57. Specialized and Composite Structures**

- 57.1 LRU/LFU cache design
- 57.2 Rope
- 57.3 Gap buffer, piece table
- 57.4 Persistent data structures (path copying, fat nodes)
- 57.5 Functional data structures, immutable lists, finger trees
- 57.6 Van Emde Boas tree
- 57.7 Link-cut trees, Euler tour trees, top trees
- 57.8 Interval trees, priority search trees
- 57.9 Dancing links (Algorithm X)
- 57.10 Bitmaps, roaring bitmaps
- 57.11 Succinct data structures (rank/select)
- 57.12 Concurrent and lock-free structures (queues, stacks, hash maps)
- 57.13 Memory allocators, memory pools, garbage-collection structures
- 57.14 Time-series and log-structured structures
- 57.15 Cache-aware and cache-oblivious design

---

## PART XI: ADVANCED ANALYSIS AND THEORY

**Ch 58. Amortized Analysis**

- 58.1 Aggregate method
- 58.2 Accounting method
- 58.3 Potential method
- 58.4 Examples: dynamic tables, binary counter, splay trees, union-find

**Ch 59. Lower Bounds**

- 59.1 Decision-tree model
- 59.2 Adversary arguments
- 59.3 Reductions for lower bounds
- 59.4 Information-theoretic bounds

**Ch 60. Complexity Theory**

- 60.1 Decision problems and formal languages
- 60.2 Classes: P, NP, co-NP, NP-complete, NP-hard, PSPACE, EXP
- 60.3 Polynomial-time reductions
- 60.4 Classic NP-complete problems (SAT, 3-SAT, Clique, Vertex Cover, Hamiltonian Cycle, TSP, Subset Sum, Partition)
- 60.5 Cook-Levin theorem
- 60.6 Computability: Turing machines, halting problem, decidability
- 60.7 Pseudo-polynomial time, strong NP-hardness

**Ch 61. Coping with Hard Problems**

- 61.1 Approximation algorithms: vertex cover, TSP, set cover, knapsack FPTAS
- 61.2 Exponential-time algorithms and exact exponential methods
- 61.3 Fixed-parameter tractable algorithms
- 61.4 Heuristics and metaheuristics: local search, simulated annealing, genetic algorithms, tabu search
- 61.5 Randomized rounding, LP relaxation
- 61.6 SAT solvers (DPLL, CDCL overview)

**Ch 62. Alternative Computation Models**

- 62.1 Online algorithms and competitive analysis (paging, ski rental)
- 62.2 Parallel and multithreaded algorithms (work/span, PRAM)
- 62.3 Distributed algorithms (overview: consensus, leader election)
- 62.4 External-memory and cache-oblivious algorithms
- 62.5 Streaming and sublinear algorithms
- 62.6 Quantum algorithms (overview: Grover, Shor)
- 62.7 Machine-learning algorithms (CLRS 4th ed. topics: gradient descent, k-means, multiplicative weights)
- 62.8 Formal languages and automata (DFA, NFA, regular, context-free)

---

## PART XII: APPLIED AND PROFESSIONAL PRACTICE

**Ch 63. Choosing and Implementing Data Structures**

- 63.1 Choosing structures by operation profile and constraints
- 63.2 Built-in/standard-library containers across languages (concepts, complexities)
- 63.3 Memory layout, cache locality, practical vs asymptotic performance
- 63.4 Benchmarking and profiling
- 63.5 Debugging data-structure bugs
- 63.6 Reading constraints → algorithm selection table

**Ch 64. DSA in Real Systems**

- 64.1 Databases: indexes (B+ tree, hash, LSM), query planning
- 64.2 Operating systems: schedulers, page replacement, file systems
- 64.3 Networking: routing algorithms, packet queues
- 64.4 Compilers: symbol tables, parsing, graph coloring for register allocation
- 64.5 Search engines: inverted index, ranking
- 64.6 Version control: DAGs, diff algorithms
- 64.7 Distributed systems: consistent hashing, Merkle trees, gossip
- 64.8 Games and graphics: spatial partitioning, pathfinding
- 64.9 Machine learning: nearest-neighbor search (k-d tree, LSH, HNSW), embeddings indexes
- 64.10 Cryptography: hashing, Merkle trees

**Ch 65. Practice and Mastery**

- 65.1 Topic-wise problem sets, basic → advanced
- 65.2 Pattern recognition drills
- 65.3 Timed problem solving, competitive programming
- 65.4 Mock interviews, whiteboard communication
- 65.5 Complexity analysis drills
- 65.6 Revision cheat sheets

---

## APPENDICES

- **A.** Summations and series
- **B.** Sets, relations, functions, graphs, trees
- **C.** Counting and probability
- **D.** Matrices
- **E.** Complexity cheat sheet (all structures and algorithms)
- **F.** Standard recurrence-solutions table
- **G.** Glossary of terms
- **H.** Recommended references (CLRS, Sedgewick-Wayne, Skiena, Kleinberg-Tardos, Dasgupta-Papadimitriou-Vazirani, Knuth TAOCP, Sipser)