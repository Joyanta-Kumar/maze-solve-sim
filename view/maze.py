from constant import ROWS, COLS
from view.cell import Cell, Wall
from utils.function import break_wall, get_neighbors
from random import choice, randint


class Maze:
  def __init__(self):
    self.grid = []
    self.cell_count = ROWS * COLS


  def generate(self):

    self.grid = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]

    next_cell = self.grid[0][0]
    visited_cell_count = 0
    stop_condition = False
    queue = []

    while not stop_condition:
      current_cell = next_cell
      if not current_cell.visited:
        current_cell.visited = True
        visited_cell_count += 1
        stop_condition = visited_cell_count == self.cell_count

      neighbors = get_neighbors(current_cell, self.grid, ignore_walls=True)
      if len(neighbors) != 0:
        next_cell = choice(neighbors)

        break_wall(current_cell, next_cell)

        if len(neighbors) > 1:
          queue.insert(0, current_cell)
          for neighbor in neighbors:
            if randint(1, 30) == 3:
              break_wall(current_cell, neighbor)
                
      elif len(queue) != 0:
        next_cell = queue.pop()
    
    for row in self.grid:
      for cell in row:
        cell.visited = False
  

  def save(self):
    with open("maze_files/maze.txt", "w") as file:
      for row in self.grid:
        for cell in row:
          file.write(str(cell) + "\n")
  
  def load(self):
    with open("maze_files/maze.txt", "r") as file:
      cell_data = ""
      grid_row = []
      last_row_number = 0

      for line in file:
        cell_data = line.strip("\n").split(" ")
        row = int(cell_data[0])
        col = int(cell_data[1])
        wall_data = cell_data[2]

        if row != last_row_number:
          last_row_number = row
          self.grid.append(grid_row)
          grid_row = []
        
        cell = Cell(row, col)
        cell.walls[Wall.TOP] = wall_data[Wall.TOP] == "1"
        cell.walls[Wall.LEFT] = wall_data[Wall.LEFT] == "1"
        cell.walls[Wall.BOTTOM] = wall_data[Wall.BOTTOM] == "1"
        cell.walls[Wall.RIGHT] = wall_data[Wall.RIGHT] == "1"

        grid_row.append(cell)
      
          


  def draw(self):
    for row in self.grid:
      for cell in row:
        cell.draw()