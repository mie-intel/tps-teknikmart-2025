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
observation_data = utils.load_json('observation_data.json')

# Initialize the cashier
cashier = Cashier()


def exit_game():
    pygame.quit()
    sys.exit()


PersonState.init()


def run():
    while True:
        if ctime // 600 >= len(observation_data):
            print("Simulation finished.")
            break
        prep_game()
        map.create_room()
        cashier.draw()
        if ctime % 60 == 0:
            PersonState.spawn_person(ctime)
        PersonState.run_all()
        draw_time(ctime + (60 * 8 + 20) * 60)
        update_game()


def prep_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit_game()
    screen.fill((20, 20, 20))


def draw_time(seconds):  # Pass the screen surface as an argument
    time_string = utils.time_string(seconds)
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
    ctime += TIME_STEP  # Increment time by 1 second
