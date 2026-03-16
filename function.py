from cell import Cell, Wall
from constant import ROWS, COLS

def get_neighbors(cell: Cell, grid: list) -> list:
  neighbors = []
  # Left
  if cell.col > 0:
    left_cell = grid[cell.row][cell.col-1]
    if not left_cell.visited:
      neighbors.append(left_cell)
  # Right
  if cell.col < COLS-1:
    right_cell = grid[cell.row][cell.col+1]
    if not right_cell.visited:
      neighbors.append(right_cell)
  # Top
  if cell.row > 0:
    top_cell = grid[cell.row-1][cell.col]
    if not top_cell.visited:
      neighbors.append(top_cell)
  # Bottom
  if cell.row < ROWS-1:
    bottom_cell = grid[cell.row+1][cell.col]
    if not bottom_cell.visited:
      neighbors.append(bottom_cell)
  return neighbors;


def break_wall(current: Cell, next: Cell):
  if current.row == next.row:
    # left or right
    if current.col < next.col:
      # right
      current.walls[Wall.RIGHT] = False
      next.walls[Wall.LEFT] = False
    else:
      #left
      current.walls[Wall.LEFT] = False
      next.walls[Wall.RIGHT] = False
  elif current.col == next.col:
    # top or bottom
    if current.row < next.row:
      # bottom
      current.walls[Wall.BOTTOM] = False
      next.walls[Wall.TOP] = False
    else:
      # top
      current.walls[Wall.TOP] = False
      next.walls[Wall.BOTTOM] = False

