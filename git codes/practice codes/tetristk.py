import tkinter as tk
import random
import time

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 1]],
    [[1, 1, 1], [1, 1, 0]]
]

SHAPES_COLORS = ["red", "green", "blue", "yellow", "purple", "cyan", "orange"]

# Initialize window
root = tk.Tk()
root.title("Tetris")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Initialize game variables
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_piece = None
current_shape = None
current_color = None
current_x = 0
current_y = 0
score = 0

# Functions
def new_piece():
    global current_piece, current_shape, current_color, current_x, current_y
    current_shape = random.choice(SHAPES)
    current_color = random.choice(SHAPES_COLORS)
    current_piece = [[1 if cell else 0 for cell in row] for row in current_shape]
    current_x = GRID_WIDTH // 2 - len(current_piece[0]) // 2
    current_y = 0

def draw_grid():
    canvas.delete("all")
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[y][x]:
                canvas.create_rectangle(
                    x * GRID_SIZE,
                    y * GRID_SIZE,
                    (x + 1) * GRID_SIZE,
                    (y + 1) * GRID_SIZE,
                    fill=grid[y][x]
                )

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
        for col in range(len(current_piece[row])):
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

def game_over():
    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="Game Over",
        font=("Helvetica", 24),
        fill="white"
    )

new_piece()

def update():
    global current_x, current_y
    if not check_collision(current_x, current_y + 1, current_piece):
        current_y += 1
    else:
        place_piece()
        if check_collision(current_x, current_y, current_piece):
            game_over()
            return
        new_piece()
    draw_grid()
    root.after(500, update)

root.after(0, update)
root.mainloop()
