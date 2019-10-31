# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"


from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __initi__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        super().move()
        if self.x0 >= self.right_limit:
            self.x0 = self.right_limit

        if self.x0 <= self.left_limit:
            self.x0 = self.right_limit


class BoundedSimulation(Simulation):

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
        steps = BoundedSimulation(0, 20,
                                  seed=seed,
                                  left_limit=left,
                                  right_limit=right_boundary)\
            .run_simulation(20)
        print(left, steps)
