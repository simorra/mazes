from typing import Iterator, List, Tuple
from cell import Cell
from wall_table import WallTable
from random import randrange
import pyglet

class Grid:
    """
    A generic grid to generate a maze on.
    
    The grid develops from left to right (as usual)
    and bottom-up (usually it goes top-down),
    in such a way that the second row is on top of the first,
    the third on top of the second and so on.
    This representation simplifies the interaction with pyglet's
    coordinate system.
    """
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.cells = [None] * rows
        for i in range(rows):
            self.cells[i] = [Cell(i*cols + j) for j in range(cols)]
        self.walls = WallTable(rows * cols)

    def __getitem__(self, key: int) -> List[Cell]:
        return self.cells[key]

    def __iter__(self) -> Iterator[Cell]:
        for i in range(self.rows):
            for j in range(self.cols):
                yield self[i][j]

    def get_by_id(self, id: int) -> Cell:
        row, col = self.id_to_coords(id)
        return self[row][col]

    def id_to_coords(self, id: int) -> Tuple[int, int]:
        """Given the id of a cell, return the corresponding coordinates."""
        return id // self.cols, id % self.cols

    def random_cell(self) -> Cell:
        return self[randrange(self.rows)][randrange(self.cols)]

    def draw(self, window: pyglet.window.Window, marked_cell: Cell = None) -> None:
        """Draw the maze on the given window."""
        pass
