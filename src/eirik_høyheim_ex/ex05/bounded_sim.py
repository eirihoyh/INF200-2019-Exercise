# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"

from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    """A class that takes in Walker, and puts on a limit of how far to the left
    and how far to the right you can go"""
    def __init__(self, start, home, left_limit, right_limit):
        if not (left_limit <= start <= right_limit):
            raise ValueError('Start most be between the left limit and the '
                             'right limit')
        if not (left_limit <= home <= right_limit):
            raise ValueError('Home most be between the left limit and the '
                             'right limit')
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        super().move()
        if self.x0 >= self.right_limit:
            self.x0 = self.right_limit

        if self.x0 <= self.left_limit:
            self.x0 = self.left_limit


class BoundedSimulation(Simulation):
    """Takes in simulation and uses bounded_walker to set a limit from left
    to right, and runs it as many times that you want"""
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        walkin = BoundedWalker(self.start, self.home, self.left_limit,
                               self.right_limit)
        num_steps = 0
        while not walkin.is_at_home():
            walkin.move()
            num_steps += 1
        return num_steps


if __name__ == "__main__":
    num_of_walk = 20
    seed = 54321
    right_boundary = 20
    left_boundary = [0, -10, -100, -1000, -10000]
    home = 20
    start = 0
    for left in left_boundary:
        steps = BoundedSimulation(home=home, start=start,
                                  seed=seed,
                                  left_limit=left,
                                  right_limit=right_boundary) \
            .run_simulation(20)
        print(left, steps)
