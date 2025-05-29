import pygame
import config
from color import *
import game


def get_boundaries(size=(200, 200), position=(0, 0)):
    """Get the boundaries of a rectangle given its size and position."""
    # Calculate grid boundaries for the obstacle
    start_x = position[0]
    start_y = position[1]
    end_x = (position[0] + size[0])
    end_y = (position[1] + size[1])

    # Ensure we don't go out of bounds
    grid_height, grid_width = game.grid.shape
    start_x = max(0, min(start_x, grid_width - 1))
    start_y = max(0, min(start_y, grid_height - 1))
    end_x = max(0, min(end_x, grid_width - 1))
    end_y = max(0, min(end_y, grid_height - 1))

    return (start_x, start_y, end_x, end_y)


def create_obstacle(color=RED, size=(200, 150), position=(100, 100)):
    """Create an obstacle at the specified location with the given size and color."""
    pos = (position[0] - size[0] / 2, position[1] - size[1] / 2)
    pygame.draw.rect(game.screen, color, (*pos, *size))
    # Update the grid to mark the obstacle's position
    start_x, start_y, end_x, end_y = get_boundaries(
        size=size, position=position)
    # game.grid[start_y:end_y+1, start_x:end_x+1] = -1
