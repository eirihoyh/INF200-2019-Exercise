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
        """takes in a start position and home position and gives out
        how many steps you have taken to get home with help from the Walker
        class"""
        pos = Walker(self.start, self.home)

        while self.home != pos.get_position():
            pos.move()

        return pos.get_steps()

    def run_simulation(self, num_walk):
        dist = []
        for sim in range(num_walk):
            dist.append(self.single_walk())

        return dist


if __name__ == "__main__":
    num_of_walk = 20
    seeds = [12345, 54321]
    starts = [0, 10]
    homes = [10, 0]

    for walk_seed0 in range(2):
        for run_2_times in range(2):

            sim = Simulation(starts[walk_seed0], homes[walk_seed0], seeds[0])
            print(sim.run_simulation(num_of_walk))

    for walk_seed1 in range(2):
        sim = Simulation(starts[walk_seed1], homes[walk_seed1], seeds[1])
        print(sim.run_simulation(num_of_walk))
