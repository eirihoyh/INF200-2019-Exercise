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
        self.position = self.position + \
                        self.board.position_adjustment(self.position) \
                        + die_roll
        # if self.position in self.board.ladders:
        #    self.position = self.board.ladders[self.position]

        # if self.position in self.board.chutes:
        #    self.position = self.board.chutes[self.position]

        # self.board.position_adjustment(self.position)

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

    def __init__(self, player_field, board=None, seed=45,
                 randomize_players=False):
        self.player_list = player_field
        if board is None:
            self.board = Board()
        else:
            self.board = board  # if board is given then the given board works
        # if randomize_players is False:
        #     pass
        if randomize_players is True:
            self.player_list = random.shuffle(self.player_list)

        self.multi_sim = None  # Stores all the results from run_simulation

        random.seed(seed)

    def single_game(self):
        """
        takes in nothing, except whats in the __init__  function.
        Returns the winner and how may steps the winner took
        """
        player_dict = {}  # empty dictionary
        for player in self.player_list:  # goes through the player_list, one
            # player at the time
            play = player(self.board)  # sets a board to a player so the game
            # starts
            while self.board.goal_reached(play.position) is False:  # as long
                # the player has not reach the goal, it will keep on going
                play.move()  # makes a move...
                player_dict[player] = play.get_steps()  # takes in the steps
                # and gets updated to the most recent step

        winner_key = min(player_dict, key=lambda k: player_dict[k])  # find the
        # winner key, who is the one with the least steps. Took this code line
        # from internet

        return player_dict[winner_key], winner_key.__name__
        # The code 'works', but winner key get returned as __main__.Player,
        # so it does not pass the testing, we have to fix that.

    def run_simulation(self, n_sims):
        """
        takes in n_sims, how many sims. Simulates the games like in
        single_game, but does not return anything, maybe make some more self
        in __init__ ?
        """
        the_best_results = []  # empty list...
        for _ in range(n_sims):  # runs n_sims times...
            the_best_results.append(self.single_game())  # runs the single_game
            # and puts the result into the_best_results list

        self.multi_sim = the_best_results  # sets multi_sim = the_best_result
        # so the Simulation class remembers the results

    def get_results(self):
        """
        :return:
        the result from run_simulation function, e.g.,
        [(10, 'Player'), (6, 'ResilientPlayer')]
        """
        return self.multi_sim  # just returns the result, does not pass the
        # test either, but returns the right thing, but only as __main__.Player
        # so we have to fix that

    def winners_per_type(self):
        """
        :return:
        how many times a player has won for each player in a dictionary, e.g.,
        {'Player': 4, 'LazyPlayer': 2, 'ResilientPlayer': 5}
        """
        winner_dict = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}
        for score, player in self.multi_sim:
            if player == 'Player':
                winner_dict['Player'] += 1
            if player == 'LazyPlayer':
                winner_dict['LazyPlayer'] += 1
            if player == 'ResilientPlayer':
                winner_dict['ResilientPlayer'] += 1

        # This code will work, but what it returns is a bit strange, but it
        # is right
        return winner_dict

    def durations_per_type(self):
        """
        :return:
        Returns a dictionary with how long each player types used, e.g.,
        {'Player': [11, 25, 13], 'LazyPlayer': [39],
        'ResilientPlayer': [8, 7, 6, 11}
        """
        duration_dict = {'Player': [], 'LazyPlayer': [], 'ResilientPlayer': []}
        for score, player in self.multi_sim:
            if player == 'Player':
                duration_dict['Player'].append(score)
            if player == 'LazyPlayer':
                duration_dict['LazyPlayer'].append(score)
            if player == 'ResilientPlayer':
                duration_dict['ResilientPlayer'].append(score)

        # I think that this will work too, basicly the same thing as in the
        # function over
        return duration_dict

    def players_per_type(self):
        """
        :return:
        Returns a diictionary of how many types of player there is, e.g.,
        {'Player': 3, 'LazyPlayer': 1, 'ResilientPlayer': 0}
        """
        # this one is very simular to the last to functions
        num_play_dict = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}
        for score, player in self.multi_sim:
            if player == 'Player':
                num_play_dict['Player'] += 1
            if player == 'LazyPlayer':
                num_play_dict['LazyPlayer'] += 1
            if player == 'ResilientPlayer':
                num_play_dict['ResilientPlayer'] += 1

        # this code works aswell, only thing is that this one, as the two
        # previus, has a weird return that we have to fix.
        # This one returned:
        # {__main__.Player: 7, __main__.LazyPlayer: 0,
        # __main__.ResilientPlayer: 3}
        # which is kind of wrong, but the code works at fortunately
        return num_play_dict


if __name__ == '__main__':

    sim = Simulation([Player, LazyPlayer, ResilientPlayer])
    print(sim.single_game())
    sim.run_simulation(10)
    print(sim.get_results())
    print(sim.winners_per_type())
    print(sim.durations_per_type())
    print(sim.players_per_type())
