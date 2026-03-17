from structure.node import Node

class Edge:
  def __init__(self, start:Node, end:Node) -> None:
    self.start:Node = start
    self.end:Node = end