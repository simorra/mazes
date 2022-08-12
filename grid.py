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
        self.cells = [Cell(i) for i in range(rows * cols)] # cells are stored in a flat array
        self.walls = WallTable(rows * cols)

    def __getitem__(self, key: int) -> Cell:
        return self.cells[key]

    def __iter__(self) -> Iterator[Cell]:
        for i in range(self.rows * self.cols):
            yield self[i]

    def coords(self, id: int) -> Tuple[int, int]:
        """Given the id of a cell, return its row and column."""
        return id // self.cols, id % self.cols

    def random_cell(self) -> Cell:
        return self[randrange(self.rows * self.cols)]

    def draw(self, window: pyglet.window.Window, marked_cell: Cell = None) -> None:
        """Draw the maze on the given window."""
        pass
