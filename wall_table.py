from typing import List, Tuple

class WallTable:
    """
    Memory efficient data structure to keep track of the
    walls existing between cells in a grid.
    """
    def __init__(self, num_cells: int) -> None:
        """
        Create a new WallTable. The total amount of cells
        in the grid must be provided, just as if the entries
        where to be stored in a matrix.
        """
        self.N = num_cells
        self.table = {}

    def add(self, id1: int, id2: int) -> None:
        """Add a wall between the cells with the given ids."""
        self.table[self.key_of(id1, id2)] = True

    def remove(self, id1: int, id2: int) -> None:
        """If present, remove the wall between the cells with the given ids."""
        if self.get(id1, id2):
            del self.table[self.key_of(id1, id2)]

    def get(self, id1: int, id2: int) -> bool:
        """
        Access the table's entry associated with the cells with
        the given ids. Returns True if there is a wall between them,
        False otherwise.
        """
        return self.table.get(self.key_of(id1, id2), False)

    def key_of(self, id1: int, id2: int) -> int:
        """Each pair of cell's ids is associated with a key, used internally."""
        # The keys are unique, except for symmetric pairs of cells,
        # which get the same key
        if id1 <= id2:
            return id1*self.N + id2
        return id2*self.N + id1

    def all_pairs(self) -> List[Tuple[int, int]]:
        """Return all the pairs of ids of cells which share a wall."""
        pairs = []
        for key in self.table:
            pairs.append((key//self.N, key%self.N))
        return pairs
