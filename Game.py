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

avg_time_spend = [0 for _ in range(28)]  # 28 minutes of simulation
avg_max_queue_size = [0 for _ in range(28)]  # 28 minutes of simulation

# Initialize the cashier
cashier = Cashier()


def exit_game():
    pygame.quit()
    sys.exit()


PersonState.init()


def run():
    while True:
        if ctime // 600 >= len(observation_data) and len(PersonState.get_persons()) == 0:
            print("Simulation finished.")
            simulation_results()
            show_results()
            break
        prep_game()
        map.create_room()
        cashier.draw(ctime)
        if ctime % 60 == 0 and ctime // 600 < len(observation_data):
            PersonState.spawn_person(ctime)
        PersonState.run_all(ctime)
        draw_time(ctime + (60 * 8 + 20) * 60)
        update_game()


def simulation_results():
    global avg_time_spend, avg_max_queue_size
    avg_time_spend = PersonState.get_total_time_spend()
    avg_max_queue_size = cashier.max_queue_size
    avg_time_spend = [np.mean(t) if t else 0 for t in avg_time_spend]
    avg_max_queue_size = [np.mean(t) if t else 0 for t in avg_max_queue_size]
    # print("Average time spend per minute:", avg_time_spend)
    # print("Average max queue size per minute:", avg_max_queue_size)


def show_results():
    import matplotlib.pyplot as plt

    # X values: 9, 19, 29, ..., up to the length of avg_time_spend
    x_values = [9 + 10 * i for i in range(len(avg_time_spend))]

    plt.figure(figsize=(12, 5))

    bar_width = 7  # Tambahkan lebar bar

    plt.subplot(1, 2, 1)
    plt.bar(x_values, avg_time_spend, color='skyblue', width=bar_width)
    plt.xlabel('Menit')
    plt.ylabel('Rata-rata Waktu (detik)')
    plt.title('Rata-rata Waktu yang Dihabiskan per 10 Menit')
    # Tampilkan hanya setiap 4 nilai pada sumbu X
    xticks_to_show = x_values[::4]
    plt.xticks(xticks_to_show, rotation=45)

    plt.subplot(1, 2, 2)
    plt.bar(x_values, avg_max_queue_size, color='salmon', width=bar_width)
    plt.xlabel('Menit')
    plt.ylabel('Rata-rata Ukuran Antrian Maksimum')
    plt.title('Rata-rata Ukuran Antrian Maksimum per 10 Menit')
    plt.xticks(xticks_to_show, rotation=45)

    plt.tight_layout()
    plt.show()


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
