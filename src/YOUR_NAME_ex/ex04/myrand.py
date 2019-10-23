# -*- coding: utf-8 -*-

__author__ = 'Eirik Høyheim'
__email__ = 'eirihoyh@nmbu.no'


class LCGRand:
    """A class that takes in a seed and calculate LCG"""
    def __init__(self, seed):
        self.a = 7**5
        self.m = (2**31)-1
        self.seed = seed

    def rand(self):
        self.seed = (self.a * (self.seed)) % self.m
        return self.seed


class ListRand:
    """Takes in a list and takes out one number at the time, from
    the first number in the list to the last number. When you have ran trough
     all the numbers in the list, you get a RuntimeError"""
    def __init__(self, numberlist):
        self.numberlist = numberlist
        self.position = 0

    def rand(self):
        if self.position == len(self.numberlist):
            raise RuntimeError
        number = self.numberlist[self.position]
        self.position += 1
        return number
