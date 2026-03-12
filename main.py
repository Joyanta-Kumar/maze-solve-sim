import pygame
from cell import Cell, Wall
from constant import BG_COLOR, CURRENT_CELL_COLOR, COLS, ROWS, WINDOW
from random import choice

pygame.init()
pygame.display.set_caption("Maze Sim")
clock = pygame.time.Clock()
grid = [[Cell(row, col) for row in range(ROWS)] for col in range(COLS)]

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        run = False

  WINDOW.fill(BG_COLOR)

  for row in grid:
    for cell in row:
      cell.draw(WINDOW)

  # swaping the backstage with the front
  pygame.display.flip()
  clock.tick(60)