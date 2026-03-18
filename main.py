import pygame
from constant import WINDOW, CLOCK, FPS
from constant import COLS, ROWS
from constant import BG_COLOR, CELL_COLOR, VISITED_CELL_COLOR, CURRENT_CELL_COLOR, STACK_CELL_COLOR, NEXT_CELL_COLOR, NEIGHBOR_CELL_COLOR, NODE_COLOR
from view.maze import Maze
from utils.function import get_neighbors
from random import choice
from structure.node import Node
from structure.edge import Edge
from structure.graph import Graph

pygame.init()
pygame.display.set_caption("Maze Sim")

maze = Maze(ROWS, COLS, False)
graph = Graph()

next_cell = maze.grid[0][0]
current_cell = None
stop_condition = False
neighbors = []
stack = []

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        run = False
      elif event.key == pygame.K_F5:
        maze.generate(False)
        stop_condition = False
        stack = []
        neighbors = []
        graph.reset()
        next_cell = maze.grid[0][0]

  if not stop_condition:
    current_cell = next_cell
    if not current_cell.visited:
      current_cell.visited = True
      maze.visited_cell_count += 1
      graph.add_node(Node(current_cell.row, current_cell.col))
      stop_condition = maze.visited_cell_count == maze.cell_count or current_cell == maze.grid[maze.rows//2][maze.cols//2]

    neighbors = get_neighbors(current_cell, maze.grid, ignore_walls=False)
    if len(neighbors) != 0:
      if len(neighbors) > 1:
        stack.append(current_cell)
      next_cell = choice(neighbors)
      for neighbor in neighbors:
        if not neighbor.visited:
          graph.add_node(Node(neighbor.row, neighbor.col))
          graph.add_edge(Edge(current_cell, neighbor))
    elif len(stack) != 0:
      next_cell = stack.pop()


  WINDOW.fill(BG_COLOR)
  maze.draw(WINDOW)
  for row in maze.grid:
    for cell in row:
      if cell.visited:
        cell.draw(WINDOW)
  
  if current_cell:
    current_cell.draw(WINDOW, CURRENT_CELL_COLOR, padding=2, wall=False)

  graph.draw(WINDOW)

  pygame.display.flip()
  CLOCK.tick(FPS)
