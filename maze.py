from cell import Cell
from function import get_neighbors
from random import choice

class Maze:
  def __init__(self, rows, cols) -> None:
    self.rows = rows
    self.cols = cols
    self.grid: list = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
    self.cell_count = self.rows * self.cols
    self.visited_cell_count = 0
    print(self)
  
  def __str__(self) -> str:
    status: str = f"{self.rows}x{self.cols} = {self.cell_count}, visited: {self.visited_cell_count}"
    return status

  def generate(self):
    current_cell= None
    next_cell:Cell = self.grid[0][0]
    stack = []

