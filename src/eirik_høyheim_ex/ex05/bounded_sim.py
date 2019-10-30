# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"

import random
from walker_sim import Walker, Simulation

class BoundedWalker:
    def __initi__(self, start, home, left_limit, right_limit):
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit


class BoundedSimulation:
    def __init__(self, start, home, seed, left_limit, right_limit):
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit
        random.seed = seed

if __name__ == "__main__":
    num_of_walk = 20
    seeds = [12345, 54321]
    right_boundary = [20]
    left_boundary = [0, -10, -100, -1000, -10000]
    home = 20
    start = 0
