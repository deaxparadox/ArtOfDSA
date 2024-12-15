# Depth First Search

The strategy followed by depth-first search is, as its name implies, to search "deeper" in the graph.

Depth-first search explores edges out of the most recently discovered vertex *v* that still has unexplored edges leaving it. Once all of *v*'s edges have been explored, the search "backtracks" to explore edges leaving the vertex from which *v* was discovered. This process continues untill we have we have discovered all the vertices that are reachable from the original source vertex. If any undiscovered vertices remain, the depth-first search selects one of them as a new source, and it repeats the search from that source. The algorithm repeats then entire process untill it has discovered every vertex.