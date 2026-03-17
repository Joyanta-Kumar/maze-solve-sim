from structure.node import Node
from structure.edge import Edge
from view.maze import Maze

class Graph:
  def __init__(self) -> None:
    self.nodes:list = []
    self.edges:list = []
  

  def draw(self, window):
    for edge in self.edges:
      edge.draw(window)

    for node in self.nodes:
      node.draw(window)
  
  def add_node(self, node: Node):
    self.nodes.append(node)
  
  def add_edge(self, edge: Edge):
    self.edges.append(edge)
  
  def reset(self):
    self.nodes = []
    self.edges = []
