import pygame
from constant import WINDOW, CLOCK, FPS
from constant import BG_COLOR
from view.maze import Maze
from structure.graph import Graph

pygame.init()
pygame.display.set_caption("Maze Sim")

maze = Maze()
graph = Graph()


run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        run = False
      elif event.key == pygame.K_g:
        maze.generate()
        graph.fetch(maze)

  WINDOW.fill(BG_COLOR)  
  maze.draw()
  graph.draw()
  pygame.display.flip()
  CLOCK.tick(FPS)
