from typing import Iterator
from grid import Grid
from cell import Cell
from disjoint_set import DisjointSet
import random

def randomized_dfs(grid: Grid) -> Iterator[Cell]:
    stack = [grid.random_cell()]
    while stack:
        curr = stack[-1]
        yield curr
        curr.visited = True
        unvisited_neighbours = list(filter(lambda cell: not cell.visited, curr.neighbours))
        if unvisited_neighbours:
            next = random.choice(unvisited_neighbours)
            grid.remove_wall(curr.id, next.id)
            stack.append(next)
        else:
            stack.pop()

def randomized_kruskal(grid: Grid) -> Iterator[Cell]:
    cell_sets = DisjointSet(grid.rows*grid.cols)
    wall_list = grid.get_all_walls()

    random.shuffle(wall_list)
    for wall in wall_list:
        if cell_sets.find(wall[0]) != cell_sets.find(wall[1]):
            c1 = grid[wall[0]]
            c2 = grid[wall[1]]
            yield c1
            grid.remove_wall(c1.id, c2.id)
            yield c2
            cell_sets.union(c1.id, c2.id)

def growing_tree(grid: Grid) -> Iterator[Cell]:
    active_cells = [grid.random_cell()]
    active_cells[0].visited = True
    while active_cells:
        idx = random.randrange(len(active_cells))
        curr = active_cells[idx]
        unvisited_neighbours = list(filter(lambda cell: not cell.visited, curr.neighbours))
        if unvisited_neighbours:
            neighbour = random.choice(unvisited_neighbours)
            yield curr
            grid.remove_wall(curr.id, neighbour.id)
            yield neighbour
            neighbour.visited = True
            active_cells.append(neighbour)
        else:
            # To get constant time complexity, always remove
            # from the end of the list. Since the elements are 
            # extracted randomly, it doesn't matter if we alter
            # their order by swapping two of them
            active_cells[idx], active_cells[-1] = active_cells[-1], active_cells[idx]
            active_cells.pop()
