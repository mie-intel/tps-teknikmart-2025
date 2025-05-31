import map
from config import *
import pygame


class Cashier:
    def __init__(self):
        self.num = CASHIER_NUM
        self.position = []
        self.size = (20, 20)
        self.queue = []
        for i in range(self.num):
            pos = (200 + i * AGENT_SIZE * 2, 100)
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
                      [1] + 10 + (AGENT_SIZE + 10) * len(self.queue[smallest_qid]))
        person.update_target(new_target)
        person.qid = smallest_qid
        person.qpos = len(self.queue[smallest_qid]) - 1

    def remove_from_queue(self, person):
        qid = person.qid
        if qid is not None and qid < len(self.queue) and person in self.queue[qid]:
            self.queue[qid].remove(person)
        # Update the target for the next person in the queue, if any

        for i in range(len(self.queue[qid])):
            next_target = (
                self.position[qid][0], self.position[qid][1] + 10 + (AGENT_SIZE + 10) * (i + 1))
            self.queue[qid][i].update_target(next_target)
            self.queue[qid][i].status = "update_queue"
            self.queue[qid][i].qpos = i

        person.update_target((500, 500))

    def get_queue_position(self):
        smallest_qid = self.get_smallest_queue_id()
        return (self.position[smallest_qid][0], self.position[smallest_qid][1] + 10 + (AGENT_SIZE + 10) * len(self.queue[smallest_qid]))
