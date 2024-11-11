import pygame
import random
from board import Board
from robot import Robot

pygame.init()

GRID_SIZE = 16
CELL_SIZE = 40
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
SCALE = 200

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WINDOW_SIZE + SCALE, WINDOW_SIZE + SCALE))
pygame.display.set_caption("Rasende Roboter")

board = Board(GRID_SIZE, CELL_SIZE, SCALE//2)
robots = [
    Robot(RED, (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))),
    Robot(BLUE, (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))),
    Robot(GREEN, (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))),
    Robot(YELLOW, (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)))
]

for robot in robots:
    robot.place_on_table(board)

target_robot = random.choice(robots)
board.target = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

font = pygame.font.SysFont('Arial', 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    objective_text = f"The {target_robot.return_color()} robot have to go in the target case"
    text_surface = font.render(objective_text, True, BLACK)
    screen.blit(text_surface, (10, 10))

    board.init_draw(screen)
    board.draw_cells(screen)

    pygame.display.flip()

pygame.quit()
