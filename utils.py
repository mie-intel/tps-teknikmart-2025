import random
import math
from config import *
import state
import numpy as np


def random_between(l, r):
    return random.random() * (r - l) + l


def random_data(mean, std_dev):
    return random_between(mean - std_dev, mean + std_dev)


def norm(v):  # Vektor normal
    return math.sqrt(v[0] ** 2 + v[1] ** 2)


def normalize(v):
    norm_v = norm(v)
    return v if norm_v == 0 else v / norm_v


def move(pos, target, SPEED):
    target = np.array(target)
    pos = np.array(pos)
    direction = normalize(target - pos)
    return tuple(target) if norm(target - pos) < SPEED * TIME_STEP else tuple(pos + direction * SPEED * TIME_STEP)


def equal_pos(a, b, tolerance=0.001):
    a = np.array(a)
    b = np.array(b)
    return norm(a - b) < tolerance + 0.01

# String Utils


def random_between_room():
    return (random_between(state.room_area[0], state.room_area[2]), random_between(state.room_area[1], state.room_area[3]))


def time_string(time_in_seconds):
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60
    minutes_string = f"0{minutes}" if minutes < 10 else f"{minutes}"
    seconds_string = f"0{seconds}" if seconds < 10 else f"{seconds}"
    return f"{minutes_string}:{seconds_string}"


def random_outside_room():
    top = random.randint(0, 1)
    if top:
        x = random_between(state.room_area[2], SCREEN_SIZE[0])
        y = random.randint(0, 1) * SCREEN_SIZE[1]
        if y == 0:
            y -= AGENT_SIZE
        else:
            y += AGENT_SIZE
    else:  # Choose left
        x = SCREEN_SIZE[0] + AGENT_SIZE
        y = random_between(0, SCREEN_SIZE[1])
    return (x, y)
