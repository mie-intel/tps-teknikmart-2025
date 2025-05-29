import pygame
from config import *
import game
import utils


class Person:
    def __init__(self, position=(0, 0), size=(AGENT_SIZE, AGENT_SIZE), color=(255, 0, 0)):
        self.position = position
        self.size = size
        self.color = color
        self.state = "shopping"
        self.current_target = (0, 0)
        # Random shopping time with mean 5 and std dev 2
        self.shopping_time = utils.random_data(80, 3)  # in seconds
        self.transaction_time = utils.random_data(70, 12)

        # Create pygame.Rect object for collision detection and positioning
        self.rect = pygame.Rect(
            position[0] - AGENT_SIZE / 2, position[1] - AGENT_SIZE / 2, size[0], size[1])

    def run(self):
        self.draw()
        self.update_state()
        self.move(self.current_target)

    def draw(self):
        """Draw the person on the given screen."""
        # Update rect position to match current position
        self.rect.x, self.rect.y = self.position
        pygame.draw.rect(game.screen, self.color, self.rect)

    def update_state(self):
        if self.state == "shopping":
            self.shopping_time -= time_step
            # Update target if reached
            if utils.equal_pos(self.position, self.current_target):
                self.update_target((utils.random_between(
                    0, SCREEN_SIZE[0]), utils.random_between(0, SCREEN_SIZE[1])))
            if self.shopping_time <= 0:
                self.state = "transaction"
                self.update_target((1, 1))
        elif self.state == "transaction":
            self.transaction_time -= time_step
            if self.transaction_time <= 0:
                self.state = "done"
        elif self.state == "done":
            self.update_target((0, 0))

    def update_target(self, target):
        print(f"Updating target from {self.current_target} to {target}")
        self.current_target = target
        self.move(target)

    def move(self, target):
        """Move the person to absolute position (x, y)."""
        self.position = utils.move(self.position, target, speed)

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
