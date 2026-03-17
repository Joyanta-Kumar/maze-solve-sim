import pygame
from constant import WINDOW, CLOCK, FPS
from constant import COLS, ROWS
from constant import BG_COLOR, CELL_COLOR, VISITED_CELL_COLOR, CURRENT_CELL_COLOR, STACK_CELL_COLOR
from view.maze import Maze
from function import get_neighbors
from random import choice

pygame.init()
pygame.display.set_caption("Maze Sim")

maze = Maze(ROWS, COLS)

next_cell = maze.grid[0][0]
queue = []
current_cell = None
stop_condition = False

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        run = False
      elif event.key == pygame.K_F5:
        maze.generate()
        queue = []
        next_cell = maze.grid[0][0]
  
  if not stop_condition:
    current_cell = next_cell
    if not current_cell.visited:
      current_cell.visited = True
      maze.visited_cell_count += 1
      stop_condition = maze.visited_cell_count == maze.cell_count

    neighbors = get_neighbors(current_cell, maze.grid, ignore_walls=False)
    if len(neighbors) != 0:
        next_cell = choice(neighbors)
        if len(neighbors) > 1:
          queue.insert(0, current_cell)
    elif len(queue) != 0 and not stop_condition:
      next_cell = queue.pop()

  WINDOW.fill(BG_COLOR)

  for row in maze.grid:
    for cell in row:
      cell.draw(WINDOW, VISITED_CELL_COLOR if cell.visited else CELL_COLOR)
  
  for cell in queue:
    cell.draw(WINDOW, STACK_CELL_COLOR, padding=40, wall=False)

  if current_cell:
    current_cell.draw(WINDOW, CURRENT_CELL_COLOR, padding=10, wall=False)

  pygame.display.flip()
  CLOCK.tick(FPS)
