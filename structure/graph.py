from structure.node import Node
from structure.edge import Edge
from view.maze import Maze
from view.cell import Cell
from utils.function import get_neighbors
from random import choice
from constant import ROWS, COLS

class Graph:
  def __init__(self) -> None:
    self.edges:list = []
  
  def draw(self):
    for edge in self.edges:
      edge.draw()
  
  def add_edge(self, edge:Edge):
    self.edges.append(edge)
  
  def reset(self):
    self.edges = []


  def fetch(self, maze:Maze):

    self.reset()
    
    next_cell = maze.grid[0][0]
    visited_cell_count = 0
    stop_condition = False
    queue = []

    while not stop_condition:

      current_cell:Cell = next_cell
      if not current_cell.visited:
        current_cell.visited = True
        visited_cell_count += 1
        stop_condition = visited_cell_count == maze.cell_count
      
      neighbors = get_neighbors(current_cell, maze.grid)
      for neighbor in neighbors:
        edge = Edge(Node(current_cell.row, current_cell.col), Node(neighbor.row, neighbor.col))
        self.add_edge(edge)

      if len(neighbors) != 0:
        next_cell = choice(neighbors)
        if len(neighbors) > 1:
          queue.insert(0, current_cell)
      elif len(queue):
        next_cell = queue.pop()

