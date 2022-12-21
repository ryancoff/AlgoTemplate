# A bipartite graph.

```
Our task is to figure out whether we can divide the nodes (i.e., people) into two sets such that there aren't any edges between nodes in the same set. Intuitively, we can think of starting a traversal over such a graph. We can put the first node into the first set and all the neighbors of the node into the second set. Now, we can move one step further to the neighbours and put their neighbours in the first set. We can perform the same process to keep alternating sets between neighbors. We can use a breadth-first search traversal to assign the set to each of the nodes.
```

## BFS
### Explore Card:

* https://leetcode.com/explore/featured/card/graph/620/breadth-first-search-in-graph/


```
A breadth-first search (BFS) is an algorithm for traversing or searching a graph. It traverses in a level-wise manner, i.e., all the nodes at the present level (say l) are explored before moving on to the nodes at the next level (l + 1), where a level's number is the distance from a starting node. BFS is implemented with a queue.
```

### Keywords

* There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive)
* The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi

# Road Path#

886 -> 785 -> 1971
