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
        cell.draw(WINDOW, CURRENT_CELL_COLOR, padding=10, border=False)
        cell.visited = True
  
  neighbors = get_neighbors(current_cell)
  if len(neighbors) != 0:
    for neighbor in neighbors:
      neighbor.draw(WINDOW, NEIGHBOR_CELL_COLOR, padding=20, border=False)
      stack.append(current_cell)
    current_cell = choice(neighbors)
  elif len(stack) != 0:
    current_cell = stack.pop()

  # swaping the backstage with the front
  pygame.display.flip()
  clock.tick(FPS)
