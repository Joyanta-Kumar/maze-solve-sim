import pygame
from constant import WINDOW, CLOCK, FPS
from constant import COLS, ROWS
from constant import BG_COLOR, CELL_COLOR, VISITED_CELL_COLOR, CURRENT_CELL_COLOR, NEXT_CELL_COLOR, NEIGHBOR_CELL_COLOR
from maze import Maze
from function import get_neighbors, break_wall
from random import choice

pygame.init()
pygame.display.set_caption("Maze Sim")

maze = Maze(ROWS, COLS)

neighbors = []
next_cell = maze.grid[0][0]
current_cell = None
stack = []

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        run = False
      elif event.key == pygame.K_SPACE:
        pass
  

  if maze.visited_cell_count != maze.cell_count and next_cell:
    break_wall(current_cell, next_cell)
    current_cell = next_cell

    if not current_cell.visited:
      current_cell.visited = True
      maze.visited_cell_count += 1
      stack.append(current_cell)
    
    neighbors = get_neighbors(current_cell, maze.grid, ignore_walls=True)
    if len(neighbors) != 0:
      next_cell = choice(neighbors)
    elif len(stack) != 0:
      next_cell = stack.pop()

  print(maze)
  WINDOW.fill(BG_COLOR)

  for row in maze.grid:
    for cell in row:
      if cell.visited:
        cell.draw(WINDOW, VISITED_CELL_COLOR)
      else:  
        cell.draw(WINDOW, CELL_COLOR)

  if current_cell:
    current_cell.draw(WINDOW, CURRENT_CELL_COLOR, wall=False)

  for neighbor in neighbors:
    neighbor.draw(WINDOW, NEIGHBOR_CELL_COLOR, padding=20, wall=False)
  
  if next_cell:
    next_cell.draw(WINDOW, NEXT_CELL_COLOR, padding=10, wall=False)

  pygame.display.flip()
  CLOCK.tick(FPS)
