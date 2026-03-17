from constant import WINDOW_PADDING, CELL_SIZE
import pygame

class Node:
  def __init__(self, row:int, col:int) -> None:
    self.row:int = row
    self.col:int = col

  def draw(self, window, color, offset_x=WINDOW_PADDING, offset_y=WINDOW_PADDING):
    x = self.col*CELL_SIZE+offset_x + CELL_SIZE // 2
    y = self.row*CELL_SIZE+offset_y + CELL_SIZE // 2
    pygame.draw.circle(window, color, (x, y), 4)