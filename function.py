from cell import Cell, Wall
from constant import ROWS, COLS

def get_neighbors(cell, grid: list, ignore_walls=False) -> list:
  neighbors = []
  # Left
  if cell.col > 0:
    left_cell:Cell = grid[cell.row][cell.col-1]
    if not left_cell.visited and (ignore_walls or (not cell.walls[Wall.LEFT] and not left_cell.walls[Wall.RIGHT])):
      neighbors.append(left_cell)
  # Right
  if cell.col < COLS-1:
    right_cell:Cell = grid[cell.row][cell.col+1]
    if not right_cell.visited and (ignore_walls or (not cell.walls[Wall.RIGHT] and not right_cell.walls[Wall.LEFT])):
      neighbors.append(right_cell)
  # Top
  if cell.row > 0:
    top_cell:Cell = grid[cell.row-1][cell.col]
    if not top_cell.visited and (ignore_walls or (not cell.walls[Wall.TOP] and not top_cell.walls[Wall.BOTTOM])):
      neighbors.append(top_cell)
  # Bottom
  if cell.row < ROWS-1:
    bottom_cell:Cell = grid[cell.row+1][cell.col]
    if not bottom_cell.visited and (ignore_walls or (not cell.walls[Wall.BOTTOM] and not bottom_cell.walls[Wall.TOP])):
      neighbors.append(bottom_cell)
  return neighbors


def break_wall(current, next):
  if current and next and current != next:
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

