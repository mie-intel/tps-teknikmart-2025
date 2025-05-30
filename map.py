import pygame
from config import *
from color import *
import Game
import state


def create_obstacle(color=RED, size=(200, 150), position=(100, 100)):
    """Create an obstacle at the specified location with the given size and color."""
    pos = (position[0] - size[0] / 2, position[1] - size[1] / 2)
    pygame.draw.rect(Game.screen, color, (*pos, *size))


# x1, y1, x2, y2
def create_room(color=WHITE, door_color=DARKGRAY, p=(0, 0, 500, 800)):
    """Create a room at the specified location with the given size and color."""
    # Left
    pygame.draw.rect(Game.screen, color, (p[0], p[1], WALL_SIZE, p[3] - p[1]))
    # Right
    pygame.draw.rect(Game.screen, color,
                     (p[2] - WALL_SIZE, p[1], WALL_SIZE, p[3] - p[1]))
    # Top
    pygame.draw.rect(Game.screen, color,
                     (p[0] + WALL_SIZE, p[1], p[2] - p[0] - WALL_SIZE * 2, WALL_SIZE))
    # Bottom
    pygame.draw.rect(Game.screen, color,
                     (p[0] + WALL_SIZE, p[3] - WALL_SIZE, p[2] - p[0] - WALL_SIZE * 2, WALL_SIZE))

    # Update state
    state.room_area = [p[0] + WALL_SIZE, p[1] +
                       WALL_SIZE, p[2] - WALL_SIZE, p[3] - WALL_SIZE]

    # Create door
    door = pygame.draw.rect(Game.screen, door_color,
                            (p[2] - WALL_SIZE * 2, (p[1] + p[3]) * 5 / 8, WALL_SIZE * 3, WALL_SIZE * 5))

    state.door = door.center
    print(f"Door position: {state.door}")
