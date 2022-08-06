from typing import Iterator
from grid import Grid
from cell import Cell
import random

def aldous_broder(grid: Grid) -> Iterator[Cell]:
    curr = grid.random_cell()
    curr.visited = True
    num_visited_cells = 1
    yield curr
    while num_visited_cells < grid.rows*grid.cols:
        neighbour = random.choice(curr.neighbours)
        if not neighbour.visited:
            grid.walls.remove(curr, neighbour)
            neighbour.visited = True
            num_visited_cells += 1
        curr = neighbour
        yield curr

def randomized_dfs(grid: Grid) -> Iterator[Cell]:
    stack = [grid.random_cell()]
    while stack:
        curr = stack[-1]
        yield curr
        curr.visited = True
        unvisited_neighbours = list(filter(lambda cell: not cell.visited, curr.neighbours))
        if unvisited_neighbours:
            next = random.choice(unvisited_neighbours)
            grid.walls.remove(curr, next)
            stack.append(next)
        else:
            stack.pop()
        