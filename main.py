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

next_cell = maze.grid[0][0]
queue = []


while maze.visited_cell_count != maze.cell_count:
  current_cell = next_cell
  if not current_cell.visited:
    current_cell.visited = True
    maze.visited_cell_count += 1

  neighbors = get_neighbors(current_cell, maze.grid, ignore_walls=True)
  if len(neighbors) != 0:
    next_cell = choice(neighbors)
    break_wall(current_cell, next_cell)
    if len(neighbors) > 1:
      queue.insert(1, current_cell)
  elif len(queue) != 0:
    next_cell = queue.pop()
  


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


  WINDOW.fill(BG_COLOR)

  for row in maze.grid:
    for cell in row: 

      cell.draw(WINDOW, VISITED_CELL_COLOR)

  pygame.display.flip()
  CLOCK.tick(FPS)
