import pygame
from config import *
import Game
import utils
import state


class Person:
    def __init__(self, position=(0, 0), size=(AGENT_SIZE, AGENT_SIZE), color=(255, 0, 0), shopping_time=0, transaction_time=0):
        self.position = position
        self.size = size
        self.color = color
        self.state = "shopping"
        self.qid = None
        self.qpos = None
        self.inside = True
        self.total_time = 0
        self.total_all_time = 0
        # Random target within the room area
        self.current_target = utils.random_between_room()
        # Random shopping time with mean 5 and std dev 2
        self.shopping_time = utils.random_data(
            200, 50) if shopping_time == 0 else shopping_time  # in seconds
        self.transaction_time = utils.random_data(
            70, 12) if transaction_time == 0 else transaction_time  # in seconds

        # Create pygame.Rect object for collision detection and positioning
        self.rect = pygame.Rect(
            position[0] - AGENT_SIZE / 2, position[1] - AGENT_SIZE / 2, size[0], size[1])

        print(
            f"Created person at {self.position} with shopping time {self.shopping_time} and transaction time {self.transaction_time}")

    def run(self):
        self.draw()
        self.update_state()
        self.move(self.current_target)

    def draw(self):
        """Draw the person on the given screen."""
        # Update rect position to match current position
        self.rect.x, self.rect.y = self.position
        pygame.draw.rect(Game.screen, self.color, self.rect)

    def update_state(self):
        if self.state == "shopping":
            self.shopping_time -= TIME_STEP
            # Update target if reached
            if utils.equal_pos(self.get_center(), self.current_target):
                self.update_target(utils.random_between_room())
            if self.shopping_time <= 0:
                self.state = "queue"
                self.update_target(Game.cashier.get_queue_position())
        elif self.state == "queue":
            # Kalo udah sampe posisi, baru masuk antrian
            if utils.equal_pos(self.get_center(), self.current_target):
                Game.cashier.add_to_queue(self)
                self.state = "update_queue"
            else:
                self.update_target(Game.cashier.get_queue_position())
        elif self.state == "update_queue":
            # Update target to the next position in the queue
            if utils.equal_pos(self.get_center(), self.current_target) and self.qpos == 0:
                self.state = "transaction"
        elif self.state == "transaction":
            self.transaction_time -= TIME_STEP
            if self.transaction_time <= 0:
                self.state = "exit"
                Game.cashier.remove_from_queue(self)
        elif self.state == "exit":
            if utils.equal_pos(self.get_center(), state.door) and self.inside:
                self.update_target(utils.random_outside_room())
                self.inside = False
            elif self.inside:
                self.update_target(state.door)
            elif self.inside == False and utils.equal_pos(self.get_center(), self.current_target):
                self.state = "done"

    def update_target(self, target):
        self.current_target = target

    def move(self, target):
        """Move the person to absolute position (x, y)."""
        new_position = utils.move(self.get_center(), target, SPEED)
        if self.state != "done" and self.state != "exit":
            self.total_time += TIME_STEP
        if self.state != "done":
            self.total_all_time += TIME_STEP
        self.position = (
            new_position[0] - self.size[0] / 2, new_position[1] - self.size[1] / 2)

    def get_center(self):
        """Get the center position of the person."""
        return (self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2)

    def check_collision(self, other_rect):
        """Check if this person collides with another rectangle."""
        return self.rect.colliderect(other_rect)
