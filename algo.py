from typing import Iterator
from grid import Grid
from cell import Cell
from disjoint_set import DisjointSet
import random

def aldous_broder(grid: Grid) -> Iterator[Cell]:
    curr = grid.random_cell()
    curr.visited = True
    num_visited_cells = 1
    yield curr
    while num_visited_cells < grid.rows*grid.cols:
        neighbour = random.choice(curr.neighbours)
        if not neighbour.visited:
            grid.remove_wall(curr.id, neighbour.id)
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