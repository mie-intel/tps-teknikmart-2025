import pygame
from config import *
import game


class Person:
    def __init__(self, position=(0, 0), size=(AGENT_SIZE, AGENT_SIZE), color=(255, 0, 0)):
        self.position = position
        self.size = size
        self.color = color

        # Create pygame.Rect object for collision detection and positioning
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        # Don't draw in __init__, leave that for the draw method

    def draw(self):
        """Draw the person on the given screen."""
        # Update rect position to match current position
        self.rect.x, self.rect.y = self.position
        pygame.draw.rect(game.screen, self.color, self.rect)

    def move(self, dx, dy):
        """Move the person by dx, dy pixels."""
        # Update position
        new_x = self.position[0] + dx
        new_y = self.position[1] + dy
        self.position = (new_x, new_y)

        # Update rect
        self.rect.x = new_x
        self.rect.y = new_y

    def move_to(self, x, y):
        """Move the person to absolute position (x, y)."""
        self.position = (x, y)
        self.rect.x = x
        self.rect.y = y

    def get_center(self):
        """Get the center position of the person."""
        return self.rect.center

    def check_collision(self, other_rect):
        """Check if this person collides with another rectangle."""
        return self.rect.colliderect(other_rect)

# Example usage:


def example_usage():
    """Example of how to use the Person class properly."""

    # Create a person
    player = Person(position=(100, 100), size=(30, 30), color=(0, 255, 0))

    # In your main game loop:
    while game.running:
        # Handle events, update game state...

        # Move the person based on input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            player.move(5, 0)
        if keys[pygame.K_UP]:
            player.move(0, -5)
        if keys[pygame.K_DOWN]:
            player.move(0, 5)

        # Clear screen
        game.screen.fill((255, 255, 255))

        # Draw the person
        player.draw(game.screen)

        # Update display
        pygame.display.flip()
