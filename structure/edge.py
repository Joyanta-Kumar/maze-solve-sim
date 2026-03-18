from structure.node import Node
from constant import WINDOW_PADDING, CELL_SIZE, EDGE_COLOR, WINDOW
import pygame

class Edge:
  def __init__(self, start:Node, end:Node):
    self.start:Node = start
    self.end:Node = end
  
  def draw(self, color=EDGE_COLOR, offset_x=WINDOW_PADDING, offset_y=WINDOW_PADDING):
    start_x = self.start.col*CELL_SIZE+offset_x + CELL_SIZE // 2
    start_y = self.start.row*CELL_SIZE+offset_x + CELL_SIZE // 2
    end_x = self.end.col*CELL_SIZE+offset_x + CELL_SIZE // 2
    end_y = self.end.row*CELL_SIZE+offset_x + CELL_SIZE // 2
    pygame.draw.line(WINDOW, color, (start_x, start_y), (end_x, end_y))
    pygame.draw.circle(WINDOW, color, (start_x, start_y), 4)
    pygame.draw.circle(WINDOW, color, (end_x, end_y), 4)