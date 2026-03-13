import pygame
from cell import Cell, Wall
from constant import BG_COLOR, CURRENT_CELL_COLOR, COLS, ROWS, WINDOW, FPS
from random import choice

pygame.init()
pygame.display.set_caption("Maze Sim")
clock = pygame.time.Clock()

grid = []

for row in range(ROWS):
  current_row = []
  for col in range(COLS):
    current_cell = Cell(row, col)
    current_row.append(current_cell)
  grid.append(current_row)

for row in grid:
  for current_cell in row:
    print([current_cell.row, current_cell.col], end="\t")
  print()

current_cell = grid[2][3]

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
  
  for row in grid:
    for cell in row:
      if cell == current_cell:
        print('['+str(cell.row), str(cell.col)+']', end="\t")
      else:
        print('', cell.row, cell.col, '', end="\t")
    print()
  print()

  WINDOW.fill(BG_COLOR)

  for row in grid:
    for cell in row:
      if (cell == current_cell):
        current_cell.draw(WINDOW, CURRENT_CELL_COLOR)
      else:
        cell.draw(WINDOW)

  # swaping the backstage with the front
  pygame.display.flip()
  clock.tick(FPS)