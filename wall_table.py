from cell import Cell

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

    def add(self, c1: Cell, c2: Cell) -> None:
        """Add a wall between c1 and c2."""
        self.table[self.key_of(c1, c2)] = True

    def remove(self, c1: Cell, c2: Cell) -> None:
        """Remove the wall between c1 and c2, if present."""
        if self.get(c1, c2):
            del self.table[self.key_of(c1, c2)]

    def get(self, c1: Cell, c2: Cell) -> bool:
        """
        Access the table's entry associated with the cells
        c1 and c2. Returns True if there is a wall between them,
        False otherwise.
        """
        return self.table.get(self.key_of(c1, c2), False)

    def key_of(self, c1: Cell, c2: Cell) -> int:
        """Each pair of cell is associated with a key, used internally."""
        # The keys are unique, except for symmetric pairs of cells,
        # which get the same key
        if c1.id <= c2.id:
            return c1.id*self.N + c2.id
        return c2.id*self.N + c1.id
