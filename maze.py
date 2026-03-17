from cell import Cell, Wall
from function import get_neighbors, break_wall
from random import choice


class Maze:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.grid: list = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
    self.cell_count = self.rows * self.cols
    self.visited_cell_count = 0
    self.generate()


  def __str__(self) -> str:
    status: str = f"{self.rows}x{self.cols} = {self.cell_count}, visited: {self.visited_cell_count}"
    return status


  def generate(self):
    for row in self.grid:
      for cell in row:
        cell.visited = False
        cell.walls[Wall.TOP] = True
        cell.walls[Wall.LEFT] = True
        cell.walls[Wall.BOTTOM] = True
        cell.walls[Wall.RIGHT] = True
    self.visited_cell_count = 0

    next_cell = self.grid[0][0]
    queue = []

    while self.visited_cell_count != self.cell_count:
      current_cell = next_cell
      if not current_cell.visited:
        current_cell.visited = True
        self.visited_cell_count += 1

      neighbors = get_neighbors(current_cell, self.grid, ignore_walls=True)
      if len(neighbors) != 0:
        next_cell = choice(neighbors)
        break_wall(current_cell, next_cell)
        if len(neighbors) > 1:
          queue.insert(1, current_cell)
      elif len(queue) != 0:
        next_cell = queue.pop()
    
    for row in self.grid:
      for cell in row:
        cell.visited = False
    self.visited_cell_count = 0
    
