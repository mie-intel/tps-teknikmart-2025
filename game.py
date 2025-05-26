import color
import numpy as np
import pygame
from config import *
import sys

pygame.init()
pygame.display.set_caption("Simulasi Teknik Mart")
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(color.WHITE)
clock = pygame.time.Clock()

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
    screen.fill(color.WHITE)


def update_game():
    pygame.display.flip()
    clock.tick(FPS)  # Limit to 60 FPS


def print_grid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()  # Print a newline for better readability
