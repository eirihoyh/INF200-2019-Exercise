# -*- coding: utf-8 -*-

__author__ = 'Eirik Høyheim'
__email__ = 'eirihoyh@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.a = 7**5
        self.m = (2**31)-1
        self.seed = seed

    def rand(self):
        self.seed = ((self.a)*(self.seed)) % self.m
        return self.seed


class ListRand:
    def __init__(self, numberlist):
        self.numberlist = numberlist
        self.position = 0

    def rand(self):
        if self.position == len(self.numberlist):
            raise RuntimeError
        number = self.numberlist[self.position]
        self.position += 1
        return number
