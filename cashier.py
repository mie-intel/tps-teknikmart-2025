import map
from config import cashier_num
import pygame


class Cashier:
    def __init__(self):
        self.num = cashier_num
        self.position = []
        self.size = (20, 20)
        self.queue = []
        for i in range(self.num):
            pos = (200 + i * 60, 100)
            self.position.append(pos)
            self.queue.append([])

    def draw(self):
        # Create Cashier
        for i in range(self.num):
            map.create_obstacle(position=self.position[i], size=self.size)

    def get_smallest_queue_id(self):
        smallest_qid = 0
        smallest_qsize = len(self.queue[0])

        for i in range(self.num):
            if len(self.queue[i]) < smallest_qsize:
                smallest_qsize = len(self.queue[i])
                smallest_qid = i

        return smallest_qid

    def add_to_queue(self, person):
        smallest_qid = self.get_smallest_queue_id()

        self.queue[smallest_qid].append(person)
        new_target = (self.position[smallest_qid][0], self.position[smallest_qid]
                      [1] + 10 + 20 * len(self.queue[smallest_qid]))
        person.update_target(new_target)

        print(
            f"Person added to queue {smallest_qid} at position {self.position[smallest_qid]} with target {person.current_target}")

    def get_queue_position(self):
        smallest_qid = self.get_smallest_queue_id()
        return (self.position[smallest_qid][0], self.position[smallest_qid][1] + 10 + 20 * len(self.queue[smallest_qid]))
