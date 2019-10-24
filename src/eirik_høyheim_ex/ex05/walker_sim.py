# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"

import random


class Walker:
    """A class that takes in your start position and the position your are
    going to. It is random if you go forward or backward, and counts how
    many steps you have to take to get to your final position"""

    def __init__(self, x0, h):
        self.x0 = x0
        self.h = h
        self.steps = 0

    def move(self):
        nextMove = random.uniform(1, 2)
        if nextMove < 1.5:
            self.x0 -= 1
        else:
            self.x0 += 1
        self.steps += 1

    def get_position(self):
        """Returns current position."""
        return self.x0

    def get_steps(self):
        """Returns number of steps taken by walker"""
        return self.steps

    def is_at_home(self):
        """Retruns True if wlaker is at home"""
        if self.x0 == self.h:
            return True
        else:
            return False


class Simulation:

    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        pos = Walker(self.start, self.home)

        while self.home != pos.get_position():
            pos.move()

        return pos.get_steps()

    def run_simulation(self, num_walk):
        dist = []
        for sim in range(num_walk):
            dist.append(Walker(self.start, self.home))

        return dist


if __name__ == "__main__":
    num_of_walk = 20
    seeds = [12345, 54321]
    home = [10, 0]
    start = [0, 10]
    for seed in seeds:
        for turns in range(2):
            simple_list = []
            t = Simulation(start[turns], home[turns], seed)
            simple_list.append(t.run_simulation(num_of_walk))
            print(simple_list)
