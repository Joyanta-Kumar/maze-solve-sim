import pygame
from cell import Cell
from constant import BG_COLOR, CURRENT_CELL_COLOR, COLS, ROWS, WINDOW, FPS, NEIGHBOR_CELL_COLOR, CLOCK, STACK_CELL_COLOR
from random import choice, randint
from function import get_neighbors, break_wall

pygame.init()
pygame.display.set_caption("Maze Sim")

grid = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]




current_cell = grid[randint(0, ROWS-1)][randint(0, COLS-1)]

stack = []

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        run = False
      elif event.key == pygame.K_h and current_cell.col > 0:
        current_cell = grid[current_cell.row][current_cell.col-1]
      elif event.key == pygame.K_l and current_cell.col < COLS-1:
        current_cell = grid[current_cell.row][current_cell.col+1]
      elif event.key == pygame.K_j and current_cell.row < ROWS-1:
        current_cell = grid[current_cell.row+1][current_cell.col]
      elif event.key == pygame.K_k and current_cell.row > 0:
        current_cell = grid[current_cell.row-1][current_cell.col]


  WINDOW.fill(BG_COLOR)

  for row in grid:
    for cell in row:
      cell.draw(WINDOW)
      if (cell == current_cell):
        cell.draw(WINDOW, CURRENT_CELL_COLOR, padding=10, border=False)
        cell.visited = True
  
  for cell in stack:
    cell.draw(WINDOW, STACK_CELL_COLOR, padding=5, border=False)

  neighbors = get_neighbors(current_cell, grid)
  next_cell = None
  if len(neighbors) != 0:
    for neighbor in neighbors:
      neighbor.draw(WINDOW, NEIGHBOR_CELL_COLOR, padding=20, border=False)
      stack.append(current_cell)
    next_cell = choice(neighbors)
    break_wall(current_cell, next_cell)
  elif len(stack) != 0:
    next_cell = stack.pop()
  
  if next_cell:
    current_cell = next_cell

  # swapping the backstage with the front
  pygame.display.flip()
  CLOCK.tick(FPS)
