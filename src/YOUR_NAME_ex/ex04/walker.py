# -*- coding: utf-8 -*-

__author__ = 'Eirik Høyheim'
__email__ = 'eirihoyh@nmbu.no'

import random


class Walker:
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

    def is_at_home(self):
        if self.x0 == self.h:
            return print('The student is home!')
        else:
            return print('The student is not home yet.')

    def get_position(self):
        return self.x0

    def get_steps(self):
        return self.steps


def walking(startpos, homepos):
    pos = Walker(startpos, homepos)

    while homepos != pos.get_position():
        pos.move()

    return pos.get_steps()


if __name__ == "__main__":
    num_sim = 5
    dist_list = [1, 2, 5, 10, 20, 50, 100]
    for distance in dist_list:
        dist = []
        for sims in range(num_sim):
            dist.append(walking(0, distance))

        print(f'Distance: {distance} -> Path lengths: {sorted(dist)}')
