import pygame
from cell import Cell
from constant import BG_COLOR, CURRENT_CELL_COLOR, COLS, ROWS, WINDOW, FPS, NEIGHBOR_CELL_COLOR
from random import choice, randint

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


def get_neighbors(cell: Cell) -> list:
  neighbors = []
  # Left
  if cell.col > 0:
    neighbors.append(grid[cell.row][cell.col-1])
  # Right
  if cell.col < COLS-1:
    neighbors.append(grid[cell.row][cell.col+1])
  # Top
  if cell.row > 0:
    neighbors.append(grid[cell.row-1][cell.col])
  # Bottom
  if cell.row < ROWS-1:
    neighbors.append(grid[cell.row+1][cell.col])
  return neighbors;




current_cell = grid[randint(0, ROWS-1)][randint(0, COLS-1)]

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
      cell.draw(WINDOW)
      if (cell == current_cell):
        current_cell.draw(WINDOW, CURRENT_CELL_COLOR, padding=10, border=False)
  
  neighbors = get_neighbors(current_cell)
  if len(neighbors) != 0:
    for neighbor in neighbors:
      neighbor.draw(WINDOW, NEIGHBOR_CELL_COLOR, padding=20, border=False)

  # swaping the backstage with the front
  pygame.display.flip()
  clock.tick(FPS)
