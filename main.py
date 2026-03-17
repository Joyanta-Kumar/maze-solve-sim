import pygame
from constant import WINDOW, CLOCK, FPS
from constant import COLS, ROWS
from constant import BG_COLOR, CELL_COLOR
from maze import Maze

pygame.init()
pygame.display.set_caption("Maze Sim")

maze = Maze(ROWS, COLS)

next_cell = maze.grid[0][0]
queue = []


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

  WINDOW.fill(BG_COLOR)

  for row in maze.grid:
    for cell in row: 
      cell.draw(WINDOW, CELL_COLOR)

  pygame.display.flip()
  CLOCK.tick(FPS)
