import pygame
from constant import WINDOW, CLOCK, FPS
from constant import COLS, ROWS
from constant import BG_COLOR, CELL_COLOR, VISITED_CELL_COLOR, CURRENT_CELL_COLOR, STACK_CELL_COLOR, NEXT_CELL_COLOR, NEIGHBOR_CELL_COLOR, NODE_COLOR
from view.maze import Maze
from function import get_neighbors
from random import choice
from structure.node import Node
from structure.edge import Edge

pygame.init()
pygame.display.set_caption("Maze Sim")

maze = Maze(ROWS, COLS)

next_cell = maze.grid[0][0]
stack = []
current_cell = None
stop_condition = False
neighbors = []

nodes = []
edges = []

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
        stack = []
        current_cell = None
        stop_condition = False
        next_cell = maze.grid[0][0]
        neighbors = []
        nodes = []
        edges = []
  
  if not stop_condition:
    current_cell = next_cell
    if not current_cell.visited:
      current_cell.visited = True
      maze.visited_cell_count += 1
      nodes.append(Node(current_cell.row, current_cell.col))
      stop_condition = maze.visited_cell_count == maze.cell_count

    neighbors = get_neighbors(current_cell, maze.grid, ignore_walls=False)
    if len(neighbors) != 0:
        next_cell = choice(neighbors)
        edges.append(Edge(current_cell, next_cell))
        if len(neighbors) > 1:
          stack.append(current_cell)
    elif len(stack) != 0 and not stop_condition:
      next_cell = stack.pop()

  WINDOW.fill(BG_COLOR)

  for row in maze.grid:
    for cell in row:
      if cell.visited:
        cell.draw(WINDOW, CELL_COLOR)
  
  for cell in stack:
    cell.draw(WINDOW, STACK_CELL_COLOR, padding=10, wall=False)

  for cell in neighbors:
    cell.draw(WINDOW, NEIGHBOR_CELL_COLOR, padding=0, wall=False)

  if current_cell:
    current_cell.draw(WINDOW, CURRENT_CELL_COLOR, padding=0, wall=False)
  
  if next_cell:
    next_cell.draw(WINDOW, NEXT_CELL_COLOR, padding=0, wall=False)
  
  for node in nodes:
    node.draw(WINDOW, NODE_COLOR)
  
  for edge in edges:
    edge.draw(WINDOW, NODE_COLOR)

  pygame.display.flip()
  CLOCK.tick(FPS)
