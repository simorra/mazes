class DisjointSet:
    """
    Implementation of the disjoint set data structure.
    It represents a set of elements which is partitioned
    in disjoint subsets. Each subset is represented by a 
    tree and the root is the representative element of 
    the subset. Find and union operations are performed 
    with optimal efficiency.
    """
    def __init__(self, size: int) -> None:
        # For each element, store the index of its parent in the tree
        self.parent = [i for i in range(size)]
        # Upper bound to the height of each tree (only relevant for root elements)
        self.rank = [0 for i in range(size)]

    def find(self, key: int) -> int:
        """Return the representative of the set to which key belongs."""
        if self.parent[key] == key: # key is the root of its tree
            return key 
        # Path compression: to speed up subsequent calls to find
        # the parent of key is set to be the root of the tree
        self.parent[key] = self.find(self.parent[key])
        return self.parent[key]

    def union(self, key1: int, key2: int) -> None:
        """Join the subsets containing key1 and key2."""
        # Find the roots
        r1 = self.find(key1)
        r2 = self.find(key2)

        # The elements are already in the same set
        if r1 == r2: 
            return

        # Union by rank: to minimize the resulting tree height, 
        # make the tree with lower rank a subtree of the other
        if self.rank[r1] < self.rank[r2]:
            self.parent[r1] = r2
        elif self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
        else:
            # When the ranks are the same, set one of the trees
            # as a child of the other and increment the rank of 
            # the latter 
            self.parent[r2] = r1 
            self.rank[r1] += 1