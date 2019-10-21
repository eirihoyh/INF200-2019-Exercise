# -*- coding: utf-8 -*-

__author__ = 'Eirik Høyheim'
__email__ = 'eirihoyh@nmbu.no'

import random


class LCGRand:
    def __init__(self, seed):
        self.a = 7**5
        self.m = (2**31)-1
        self.n = 0
        self.seed = seed

    def rand(self):
        pass


class ListRand:
    def __init__(self, numberlist):
        self.numberlist = numberlist
        self.position = 0

    def rand(self):
        try:
            k = self.numberlist[self.position]
            self.position += 1
            return k
        except RuntimeError:
            print('The list is empty')
