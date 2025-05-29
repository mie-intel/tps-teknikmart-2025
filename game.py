import color
import numpy as np
import pygame
from config import *
import sys
import state
import utils
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


def run_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit_game()
    screen.fill((20, 20, 20))


def draw_time():  # Pass the screen surface as an argument
    time_string = utils.time_string(state.ctime)
    font = pygame.font.Font(None, 45)  # Font size 18px
    text = font.render(time_string, True, color.WHITE)
    text_width = text.get_width()
    text_x = 500 - (text_width // 2)

    # Blit text at position (500, 900)
    screen.blit(text, (text_x, 700))


def update_game():
    pygame.display.flip()
    clock.tick(FPS)  # Limit to 60 FPS
    state.ctime += 1


def print_grid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()  # Print a newline for better readability
