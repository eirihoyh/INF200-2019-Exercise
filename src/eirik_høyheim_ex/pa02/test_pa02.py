# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim, Meenbet A.Delele"
__email__ = "eirihoyh@nmbu.no, mesenbea@nmbu.no"

import chutes_simulation as cs

import pytest
import unittest


class TestBoard:
    """

    Tests for Board class.

    """
    def test_constructor_default(self):
        """Default constructor callable."""
        b = cs.Board()
        assert isinstance(b, cs.Board)

    def test_constructor_args(self):
        """Constructor with unnamed arguments callable."""
        b = cs.Board([(1, 4), (5, 16)], [(9, 2), (12, 3)], 90)
        assert isinstance(b, cs.Board)

    def test_constructor_named_args(self):
        """Constructor with kw args callable."""
        b = cs.Board(ladders=[(1, 4), (5, 16)], chutes=[(9, 2), (12, 3)], goal=90)
        assert isinstance(b, cs.Board)

        # The following test asserts if the user gives the right value for
        # the ladders start and end values
        start_end_ladder = [[st, end] for st, end in self.ladders]
        assert start_end_ladder[0] < start_end_ladder[1]

        # The following test asserts if the user gives the right value for
        #   the chutes start and end values
        start_end_chutes = [[st, end] for st, end in self.chutes]
        assert start_end_chutes[0] > start_end_chutes[1]

        # this asserts if the goal is > 0
        assert self.goal > 0
        if not isinstance(b, cs.Board):
            raise TypeError('Please provide the right value for '
                            'chutes, ladders or goal')

    def test_goal_reached(self, position):
        """goal_reached() callable and returns bool"""
        b = cs.Board()
        assert isinstance(b.goal_reached(1), bool)
        if b.goal_reached(1):
            result = b.goal_reached(1)
            assert result == True

    def test_position_adjustment(self):
        """position_adjustment callable and returns number"""
        b = cs.Board()
        assert isinstance(b.position_adjustment(1), (int, float))


class TestPlayer:
    def test_move(self):
        """Player has move() method, moves forward and if steps gets added"""

        b = cs.Board()
        p = cs.Player(b)
        assert 0 == p.get_steps()
        assert 0 == p.get_position()
        p.move()
        assert 0 < p.get_position()
        assert 0 < p.get_steps()


class TestResilientPlayer:

    def test_constructor(self):
        """ResilientPlayer can be created."""

        b = cs.Board()

        p = cs.ResilientPlayer(b, extra_steps=4)

        assert isinstance(p, cs.ResilientPlayer)

        assert isinstance(p, cs.Player)

    def test_move(self):
        """ResilientPlayer can move."""

        b = cs.Board()
        p = cs.ResilientPlayer(b)
        assert 0 == p.get_steps()
        assert 0 == p.get_position()
        p.move()
        assert 0 < p.get_position()
        assert 0 < p.get_steps()


class TestLazyPlayer:

    def test_constructor(self):
        """LazyPlayer can be constructed."""

        b = cs.Board()
        p = cs.LazyPlayer(b, dropped_steps=3)
        assert isinstance(p, cs.LazyPlayer)
        assert isinstance(p, cs.Player)

    def test_move(self):
        """LazyPlayer can move."""

        b = cs.Board()
        p = cs.LazyPlayer(b)
        assert 0 == p.get_steps()
        assert 0 == p.get_position()
        p.move()
        assert 0 < p.get_position()
        assert 0 < p.get_steps()
        k = cs.Player(b)


class TestSimulation:
    """Tests for Simulation class."""

    def test_run_simulation(self):
        """run_simulation() can be called"""

        s = cs.Simulation([cs.Player, cs.Player])
        assert s.multi_sim is None
        s.run_simulation(2)
        assert s.multi_sim is not None

    def test_get_results(self):
        s = cs.Simulation([cs.Player, cs.ResilientPlayer])
        s.run_simulation(3)
        r = s.get_results()
        assert isinstance(r, list)

    def test_single_game(self):
        """single_game() returns non-negative number and class name"""

        s = cs.Simulation([cs.Player, cs.Player])

        nos, wc = s.single_game()

        assert nos > 0

        assert wc == 'Player'
        s450 = cs.Simulation(7, board=None, seed=450, randomize_players=False)
        assert s450.single_game() == (11, 'Player')

    def test_simulation_results(self):
        """
        - Multiple calls to run_simulation() aggregate results
        - get_results() returns list of result tuples
        """
        s = cs.Simulation([cs.Player, cs.Player])
        s.run_simulation(2)
        r = s.get_results()
        assert len(r) == 2
        s.run_simulation(1)
        r = s.get_results()
        assert len(r) == 3
        assert all(s > 0 and t == 'Player' for s, t in r)

        player_list = 7
        s450 = cs.Simulation(player_list, board=None, seed=450,
                             randomize_players=False)

        assert s450.get_results() == [
            (16, 'Player'), (16, 'Player'), (34, 'LazyPlayer'),
            (24, 'ResilientPlayer'), (18, 'ResilientPlayer'),
            (8, 'ResilientPlayer'), (30, 'LazyPlayer')
        ]

    def test_players_per_type(self):
        """player_per_type() returns dict mapping names to non-neg numbers."""

        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])

        p = s.players_per_type()

        assert all(k in ['Player', 'LazyPlayer', 'ResilientPlayer']

                   for k in p.keys())

        assert all(v >= 0 for v in p.values())

        player_list = 7
        s450 = cs.Simulation(player_list, board=None, seed=450,
                             randomize_players=False)
        assert s450.players_per_type() == {
            'Player': 1, 'LazyPlayer': 1, 'ResilientPlayer': 1
        }

    def test_winners_per_type(self):
        """winners_per_type() returns dict mapping names to non-neg numbers."""
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        s.run_simulation(10)
        w = s.winners_per_type()
        assert all(k in ['Player', 'LazyPlayer', 'ResilientPlayer']
                   for k in w.keys())
        assert all(v >= 0 for v in w.values())

        player_list = 7
        s450 = cs.Simulation(player_list, board=None, seed=450,
                             randomize_players=False)
        assert s450.winners_per_type() == {
            'Player': 2, 'LazyPlayer': 2, 'ResilientPlayer': 3
        }

    def test_durations_per_type(self):
        """

        durations_per_type() returns dict mapping names to list of

        non-neg numbers.

        """

        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])

        s.run_simulation(10)

        w = s.durations_per_type()

        assert all(k in ['Player', 'LazyPlayer', 'ResilientPlayer']

                   for k in w.keys())

        assert all(len(v) >= 0 for v in w.values())

        assert all(n >= 0 for v in w.values() for n in v)
        player_list = 7
        s450 = cs.Simulation(player_list, board=None, seed=450,
                             randomize_players=False)

        assert s450.durations_per_type() == {
            'Player': [16, 16], 'LazyPlayer': [34, 30],
            'ResilientPlayer': [24, 18, 8]
        }
