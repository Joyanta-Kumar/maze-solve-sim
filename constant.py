import pygame

# Catppuccin Mocha colors
BASE = pygame.Color(30, 30, 46)
MANTLE = pygame.Color(24, 24, 37);
CRUST = pygame.Color(17, 17, 27)

TEXT = pygame.Color(205, 214, 244)
SUBTEXT = pygame.Color(166, 173, 200)

RED = pygame.Color(243, 139, 168)
PEACH = pygame.Color(250, 179, 135)
YELLOW = pygame.Color(249, 226, 175)
GREEN = pygame.Color(166, 227, 161)
TEAL = pygame.Color(148, 226, 213)
BLUE = pygame.Color(137, 180, 250)
MAUVE = pygame.Color(203, 166, 247)
LAVENDER = pygame.Color(180, 190, 254)

BG_COLOR = pygame.Color(0, 0, 0)
WALL_COLOR = LAVENDER
FLOOR_COLOR = CRUST
CURRENT_CELL_COLOR = RED
VISITED_CELL_COLOR = BASE

# Grid
CELL_SIZE = 100

# Window
WINDOW_WIDTH = 820
WINDOW_HEIGHT = 620

COLS = WINDOW_WIDTH // CELL_SIZE
ROWS = WINDOW_HEIGHT // CELL_SIZE

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 12
