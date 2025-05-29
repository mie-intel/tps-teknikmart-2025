import random
import math
from config import *
import numpy as np


def random_between(l, r):
    print("RANDOM", random.random())
    return random.random() * (r - l) + l


def random_data(mean, std_dev):
    return random_between(mean - std_dev, mean + std_dev)


def norm(v):  # Vektor normal
    return math.sqrt(v[0] ** 2 + v[1] ** 2)


def normalize(v):
    norm_v = norm(v)
    return v if norm_v == 0 else v / norm_v


def move(pos, target, speed):
    target = np.array(target)
    pos = np.array(pos)
    direction = normalize(target - pos)
    return tuple(target) if norm(target - pos) < speed * time_step else tuple(pos + direction * speed * time_step)


def equal_pos(a, b, tolerance=0.001):
    a = np.array(a)
    b = np.array(b)
    return norm(a - b) < tolerance + 0.01

# String Utils


def time_string(time_in_seconds):
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60
    minutes_string = f"0{minutes}" if minutes < 10 else f"{minutes}"
    seconds_string = f"0{seconds}" if seconds < 10 else f"{seconds}"
    return f"{minutes_string}:{seconds_string}"
