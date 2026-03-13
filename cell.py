import pygame
from enum import IntEnum
from constant import WALL_COLOR, FLOOR_COLOR, VISITED_CELL_COLOR, CELL_SIZE

class Wall(IntEnum):
  TOP = 0
  LEFT = 1
  BOTTOM = 2
  RIGHT = 3

class Cell:

  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.walls = [True, True, True, True] # top, left, bottom, right
    self.visited = False

  def draw(self, window, color=FLOOR_COLOR, offset_x=10, offset_y=10, padding=0, border=True):
    x = offset_x + self.col * CELL_SIZE
    y = offset_y + self.row * CELL_SIZE
    if color == FLOOR_COLOR and self.visited:
      color = VISITED_CELL_COLOR
    pygame.draw.rect(window, color, (x+padding, y+padding, CELL_SIZE-padding*2, CELL_SIZE-padding*2))

    # Drawing the walls
    if border:
      if self.walls[Wall.TOP]:
        pygame.draw.line(window, WALL_COLOR, (x, y), (x+CELL_SIZE, y))
      if self.walls[Wall.BOTTOM]:
        pygame.draw.line(window, WALL_COLOR, (x, y+CELL_SIZE), (x+CELL_SIZE, y+CELL_SIZE))
      if self.walls[Wall.LEFT]:
        pygame.draw.line(window, WALL_COLOR, (x, y), (x, y+CELL_SIZE))
      if self.walls[Wall.RIGHT]:
        pygame.draw.line(window, WALL_COLOR, (x+CELL_SIZE, y), (x+CELL_SIZE, y+CELL_SIZE))




  