import pygame
from enum import IntEnum
from constant import WALL_COLOR, CELL_SIZE, WINDOW_PADDING, CELL_COLOR, WINDOW

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

  def draw(self, color=CELL_COLOR, offset_x=WINDOW_PADDING, offset_y=WINDOW_PADDING, padding=0, wall=True):
    x = offset_x + self.col * CELL_SIZE
    y = offset_y + self.row * CELL_SIZE

    pygame.draw.rect(WINDOW, color, (x+padding, y+padding, CELL_SIZE-padding*2, CELL_SIZE-padding*2))

    # Drawing the walls
    if wall:
      if self.walls[Wall.TOP]:
        pygame.draw.line(WINDOW, WALL_COLOR, (x, y), (x+CELL_SIZE, y))
      if self.walls[Wall.BOTTOM]:
        pygame.draw.line(WINDOW, WALL_COLOR, (x, y+CELL_SIZE), (x+CELL_SIZE, y+CELL_SIZE))
      if self.walls[Wall.LEFT]:
        pygame.draw.line(WINDOW, WALL_COLOR, (x, y), (x, y+CELL_SIZE))
      if self.walls[Wall.RIGHT]:
        pygame.draw.line(WINDOW, WALL_COLOR, (x+CELL_SIZE, y), (x+CELL_SIZE, y+CELL_SIZE))


  def __str__(self) -> str:
    status: str = f"{self.row} {self.col} "
    status += f"{1 if self.walls[Wall.TOP] else 0}"
    status += f"{1 if self.walls[Wall.LEFT] else 0}"
    status += f"{1 if self.walls[Wall.BOTTOM] else 0}"
    status += f"{1 if self.walls[Wall.RIGHT] else 0}"
    return status

  