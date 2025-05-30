import time
import pygame
import color
import sys
import numpy as np
import utils
import map

from config import *
from state import *
from cashier import Cashier

pygame.init()
pygame.display.set_caption("Simulasi Teknik Mart")
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(color.WHITE)
clock = pygame.time.Clock()
# mean and standard deviation for random number generation
data = [[5, 2]]

# Initialize the cashier
cashier = Cashier()

grid = np.zeros(
    (SCREEN_SIZE[0] // 50, SCREEN_SIZE[1] // 50), dtype=int)


def exit_game():
    pygame.quit()
    sys.exit()


PersonState.init()


def run():
    while True:
        prep_game()
        map.create_room()
        cashier.draw()
        PersonState.run_all()
        draw_time()
        update_game()


def prep_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit_game()
    screen.fill((20, 20, 20))


def draw_time():  # Pass the screen surface as an argument
    time_string = utils.time_string(ctime)
    font = pygame.font.Font(None, 45)  # Font size 18px
    text = font.render(time_string, True, color.WHITE)
    text_width = text.get_width()
    text_x = 500 + (text_width)

    # Blit text at position (500, 900)
    screen.blit(text, (text_x, 700))


def update_game():
    global ctime
    pygame.display.flip()
    clock.tick(FPS)  # Limit to 60 FPS
    ctime += 60 // FPS  # Increment time by 1 second


def print_grid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()  # Print a newline for better readability
