import pygame
from config import *
from color import *
import Game
import state


def get_boundaries(size=(200, 200), position=(0, 0)):
    """Get the boundaries of a rectangle given its size and position."""
    # Calculate grid boundaries for the obstacle
    start_x = position[0]
    start_y = position[1]
    end_x = (position[0] + size[0])
    end_y = (position[1] + size[1])

    # Ensure we don't go out of bounds
    grid_height, grid_width = Game.grid.shape
    start_x = max(0, min(start_x, grid_width - 1))
    start_y = max(0, min(start_y, grid_height - 1))
    end_x = max(0, min(end_x, grid_width - 1))
    end_y = max(0, min(end_y, grid_height - 1))

    return (start_x, start_y, end_x, end_y)


def create_obstacle(color=RED, size=(200, 150), position=(100, 100)):
    """Create an obstacle at the specified location with the given size and color."""
    pos = (position[0] - size[0] / 2, position[1] - size[1] / 2)
    pygame.draw.rect(Game.screen, color, (*pos, *size))
    # Update the grid to mark the obstacle's position
    start_x, start_y, end_x, end_y = get_boundaries(
        size=size, position=position)
    # Game.grid[start_y:end_y+1, start_x:end_x+1] = -1


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
