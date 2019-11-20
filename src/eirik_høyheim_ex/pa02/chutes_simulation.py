# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"
__author__ = "Meenbet A.Delele"
__email__ = "mesenbea@nmbu.no"
import random


class Board:
    default_ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    default_chutes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    def __init__(self, ladders=None, chutes=None, goal=90):
        self.ladders = ladders
        if self.ladders is None:
            self.ladders = self.default_ladders
        self.chutes = chutes
        if self.chutes is None:
            self.chutes = self.default_chutes
        self.goal = goal

    def goal_reached(self, position):
        return position >= self.goal

    def position_adjustment(self, position):
        if position in self.ladders:
            return self.ladders[position] - position
        if position in self.chutes:
            return position - self.chutes[position]
        if position not in self.ladders or self.chutes:
            return position - position


class Player:

    def __init__(self, board):
        self.board = board
        self.position = 0
        self.n_steps = 0

    def move(self):
        die_roll = random.randint(1, 6)
        self.position = self.position + \
                        self.board.position_adjustment(self.position) \
                        + die_roll
        # if self.position in self.board.ladders:
        #    self.position = self.board.ladders[self.position]

        # if self.position in self.board.chutes:
        #    self.position = self.board.chutes[self.position]

        # self.board.position_adjustment(self.position)

        self.n_steps += 1

    def check_in_goal(self):
        return self.position >= self.board.goal

    def get_steps(self):
        return self.n_steps


class ResilientPlayer(Player):
    default_extra_steps = 1

    def __init__(self, board, extra_steps=None):
        super().__init__(board)
        self.extra_steps = extra_steps
        if self.extra_steps is None:
            self.extra_steps = self.default_extra_steps

    def move(self):
        """I think that something is wrong with this code
        but can't see it rn"""
        super().move()
        if self.board.position_adjustment(self.position) < 0:
            self.position += self.extra_steps  # maybe something like this?
            # gives the player the extra step in "advance"


class LazyPlayer(Player):
    default_dropped_steps = 1

    def __init__(self, board, dropped_steps=None):
        super().__init__(board)
        self.dropped_steps = dropped_steps
        if self.dropped_steps is None:
            self.dropped_steps = self.default_dropped_steps

    def move(self):
        """I think that something is wrong with this code
        but can't see it rn"""
        orig_pos = self.position
        super().move()
        if orig_pos > self.position:
            self.position = orig_pos  # IOW, if the player goes backwards after
            # climbing a ladder, we just set the position back to the orig_pos,
            # witch we had before the throw
        if self.board.position_adjustment(self.position) > 0:
            self.position -= self.dropped_steps


class Simulation:

    def __init__(self, player_list, board=None, seed=45,
                 randomize_players=False):
        if board is None:
            board = Board()
            self.player_list = [
                player(board) for player in player_list
            ]
        else:
            self.player_list = [
                player(board) for player in player_list
            ]
        if randomize_players is False:
            pass
        if randomize_players is True:
            self.player_list = random.shuffle(self.player_list)

        random.seed(seed)

    def single_game(self):
        """
        takes in nothing, except whats in the __init__  function.
        Returns the winner and how may steps the winner took
        """
        dicts = {}
        for player in self.player_list:
            dicts[player.n_steps] = player
            while player.check_in_goal() :
                player.move()

        return print(dicts)  # very unsure if it works, not able to test

    def run_simulation(self, n_sims):
        """
        takes in n_sims, how many sims. Simulates the games like in
        single_game, but does not return anything, maybe make some more self
        in __init__ ?
        """
        pass

    def get_results(self):
        """
        :return:
        the result from run_simulation function, e.g.,
        [(10, 'Player'), (6, 'ResilientPlayer')]
        """
        pass

    def winners_per_type(self):
        """
        :return:
        how many times a player has won for each player in a dictionary, e.g.,
        {'Player': 4, 'LazyPlayer': 2, 'ResilientPlayer': 5}
        """
        pass

    def durations_per_type(self):
        """
        :return:
        Returns a dictionary with how long each player types used, e.g.,
        {'Player': [11, 25, 13], 'LazyPlayer': [39],
        'ResilientPlayer': [8, 7, 6, 11}
        """
        pass

    def players_per_type(self):
        """
        :return:
        Returns a diictionary of how many types of player there is, e.g.,
        {'Player': 3, 'LazyPlayer': 1, 'ResilientPlayer': 0}
        """
        pass
