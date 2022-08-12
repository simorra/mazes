from grid import Grid
from cell import Cell
import pyglet
from pyglet import shapes

class SquareGrid(Grid):
    """A grid in which each cell is a square"""
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)
        # Init neighbours and walls
        for cell in self:
            if south_cell := self.south(cell):
                cell.neighbours.append(south_cell)
                self.walls.add(cell, south_cell)
            if west_cell := self.west(cell):
                cell.neighbours.append(west_cell)
                self.walls.add(cell, west_cell)
            if north_cell := self.north(cell):
                cell.neighbours.append(north_cell)
                self.walls.add(cell, north_cell)
            if east_cell := self.east(cell):
                cell.neighbours.append(east_cell)
                self.walls.add(cell, east_cell)

    def south(self, cell: Cell) -> Cell:
        """Return the cell below the given one."""
        if cell.id < self.cols: # first row
            return None
        return self[cell.id - self.cols]
    
    def west(self, cell: Cell) -> Cell:
        """Return the cell to the left of the given one."""
        if cell.id % self.cols == 0: # first column
            return None
        return self[cell.id - 1]

    def north(self, cell: Cell) -> Cell:
        """Return the cell above the given one."""
        if cell.id >= (self.rows-1) * self.cols: # last row
            return None
        return self[cell.id + self.cols]

    def east(self, cell: Cell) -> Cell:
        """Return the cell to the right of the given one."""
        if cell.id % self.cols == self.cols-1: # last column
            return None
        return self[cell.id + 1]

    def draw(self, window: pyglet.window.Window, marked_cell: Cell = None) -> None:
        w_width, w_height = window.get_size()
        cell_size = min(w_width // self.cols, 
                        w_height // self.rows)
        padding_x = (w_width - self.cols*cell_size) // 2
        padding_y = (w_height - self.rows*cell_size) // 2

        batch = pyglet.graphics.Batch()
        to_draw = [] # the shapes to draw in one batch
        # Draw the grid's borders
        to_draw.append(shapes.BorderedRectangle(padding_x, padding_y, 
            cell_size*self.cols, cell_size*self.rows, border=3,
            color=(0, 0, 0), border_color=(220, 220, 220), batch=batch))
        # Draw the inner walls
        for cell in self:
            row, col = self.coords(cell.id)
            # Get the coordinates of the bottom left corner of the cell
            x_base = col*cell_size + padding_x
            y_base = row*cell_size + padding_y

            # Draw only the northen and eastern inner walls
            if row < self.rows-1 and self.walls.get(cell, self.north(cell)): # north
                to_draw.append(shapes.Line(x_base, y_base + cell_size,
                    x_base + cell_size, y_base + cell_size,
                    color=(220, 220, 220), batch=batch))
            if col < self.cols-1 and self.walls.get(cell, self.east(cell)): # east
                to_draw.append(shapes.Line(x_base + cell_size, y_base,
                    x_base + cell_size, y_base + cell_size,
                    color=(220, 220, 220), batch=batch))
        # Mark the specified cell with a dot
        if marked_cell:
            row, col = self.coords(marked_cell.id)
            # Get the coordinates of the center of the cell
            x = col*cell_size + cell_size//2 + padding_x
            y = row*cell_size + cell_size//2 + padding_y
            to_draw.append(shapes.Circle(x, y, cell_size//4, segments=30,
                color=(255, 204, 0), batch=batch))
        batch.draw()
