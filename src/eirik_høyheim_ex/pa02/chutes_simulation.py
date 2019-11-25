# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim, Meenbet A.Delele"
__email__ = "eirihoyh@nmbu.no, mesenbea@nmbu.no"

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
        return bool(position >= self.goal)

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
        self.position = (self.position +
                         self.board.position_adjustment(
                             self.position) + die_roll)
        self.n_steps += 1

    def get_position(self):
        return self.position

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
            self.position += self.extra_steps


class LazyPlayer(Player):
    default_dropped_steps = 1
    
    def __init__(self, board, dropped_steps=None):
        super().__init__(board)
        self.dropped_steps = dropped_steps
        if self.dropped_steps is None:
            self.dropped_steps = self.default_dropped_steps

    def move(self):
        orig_pos = self.position
        super().move()
        if self.board.position_adjustment(self.position) > 0:
            self.position -= self.dropped_steps
        if orig_pos > self.position:
            self.position = orig_pos  # if the player goes backwards after
            # climbing a ladder, we just set the position back to the orig_pos,
            # witch we had before the throw


class Simulation:
    def __init__(self, player_field, board=None, seed=450,
                 randomize_players=False):
        self.player_list = player_field
        self.board = board if board is not None else Board()
        if randomize_players is True:
            self.player_list = random.shuffle(self.player_list)
        self.multi_sim = None  # Makes it easier to test
        self.the_best_results = []
        self.P_type = [player.__name__ for player in self.player_list or []]
        random.seed(seed)

    def single_game(self):
        """
        takes in nothing, except whats in the __init__  function.
        Returns the winner and how may steps the winner took
        """

        players = [player(self.board) for player in self.player_list]

        while True:
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.n_steps, type(player).__name__

    def run_simulation(self, n_sims):
        """
        takes in n_sims, how many sims. Simulates the games like in
        single_game, but does not return anything, maybe make some more self
        in __init__ ?
        """

        for _ in range(n_sims):  # runs n_sims times...
            self.the_best_results.append(
                self.single_game())  # runs the single_game
            # and puts the result into the_best_results list
        self.multi_sim = self.the_best_results  # makes it easier to test...

    def get_results(self):
        """
        :return:
        the result from run_simulation function, e.g.,
        [(10, 'Player'), (6, 'ResilientPlayer')]
        """

        return self.the_best_results

    def winners_per_type(self):
        """
        :return:
        how many times a player has won for each player in a dictionary, e.g.,
        {'Player': 4, 'LazyPlayer': 2, 'ResilientPlayer': 5}
        """

        winner_types = list(zip(*self.the_best_results))[1]
        return {player_type: winner_types.count(player_type)
                for player_type in self.P_type}

    def durations_per_type(self):
        """
        :return:
        Returns a dictionary with how long each player types used, e.g.,
        {'Player': [11, 25, 13], 'LazyPlayer': [39],
        'ResilientPlayer': [8, 7, 6, 11}
        """
        duration_dict = {'Player': [], 'LazyPlayer': [], 'ResilientPlayer': []}
        for score, player in self.the_best_results:
            if player == 'Player':
                duration_dict['Player'].append(score)
            if player == 'LazyPlayer':
                duration_dict['LazyPlayer'].append(score)
            if player == 'ResilientPlayer':
                duration_dict['ResilientPlayer'].append(score)

        return duration_dict

    def players_per_type(self):
        """
        :return:
        Returns a diictionary of how many types of player there is, e.g.,
        {'Player': 3, 'LazyPlayer': 1, 'ResilientPlayer': 0}
        """
        num_play_dict = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}
        for player in self.player_list:
            if player == Player:
                num_play_dict['Player'] += 1
            if player == LazyPlayer:
                num_play_dict['LazyPlayer'] += 1
            if player == ResilientPlayer:
                num_play_dict['ResilientPlayer'] += 1

        return num_play_dict


if __name__ == '__main__':
    sim = Simulation([Player, LazyPlayer, ResilientPlayer])
    print(sim.single_game())
    sim.run_simulation(7)
    print(sim.get_results())
    print(sim.winners_per_type())
    print(sim.durations_per_type())
    print(sim.players_per_type())
