#Tetris game using a different algorithm, we can use a grid-based approach and update the game logic to handle piece movement and collisions.


import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 1]],
    [[1, 1, 1], [1, 1, 0]]
]

SHAPES_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 128, 128)

# Initialize window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Initialize game variables
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_piece = None
current_color = None
current_x = 0
current_y = 0
score = 0

# Functions
def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def new_piece():
    global current_piece, current_color, current_x, current_y
    current_shape = random.choice(SHAPES)
    current_color = SHAPES_COLORS[SHAPES.index(current_shape)]
    current_piece = current_shape
    current_x = GRID_WIDTH // 2 - len(current_piece[0]) // 2
    current_y = 0

def check_collision(x, y, shape):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if (
                    x + col < 0
                    or x + col >= GRID_WIDTH
                    or y + row >= GRID_HEIGHT
                    or grid[y + row][x + col]
                ):
                    return True
    return False

def place_piece():
    global score
    for row in range(len(current_piece)):
        for col in range(len(current_piece[row]):
            if current_piece[row][col]:
                grid[current_y + row][current_x + col] = current_color
    line_cleared = True
    while line_cleared:
        line_cleared = False
        for row in range(GRID_HEIGHT - 1, -1, -1):
            if all(grid[row]):
                line_cleared = True
                score += 100
                for y in range(row, 0, -1):
                    grid[y] = grid[y - 1][:]
                grid[0] = [0] * GRID_WIDTH
    new_piece()

def rotate_piece():
    global current_piece
    current_piece = [list(row) for row in zip(*reversed(current_piece))]

new_piece()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not check_collision(current_x - 1, current_y, current_piece):
                current_x -= 1
            if event.key == pygame.K_RIGHT and not check_collision(current_x + 1, current_y, current_piece):
                current_x += 1
            if event.key == pygame.K_DOWN and not check_collision(current_x, current_y + 1, current_piece):
                current_y += 1
            if event.key == pygame.K_UP:
                rotated = [list(row) for row in zip(*reversed(current_piece))
                if not check_collision(current_x, current_y, rotated):
                    current_piece = rotated

    if not check_collision(current_x, current_y + 1, current_piece):
        current_y += 1
    else:
        place_piece()

    screen.fill(BLACK)
    draw_grid()
    pygame.display.update()

pygame.quit()
