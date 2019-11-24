# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim, Meenbet A.Delele"
__email__ = "eirihoyh@nmbu.no, mesenbea@nmbu.no"

import chutes_simulation as cs

import pytest


class TestBoard:
    """
    Tests for Board class.
    """
    def test_default_ladders_start_smaller_than_end(self):
        """
        Tests if the default ladders makes sense, in other words
        that the start is smaller than the end
        """
        b = cs.Board()
        for idx, key in enumerate(b.default_ladders):
            assert b.default_ladders[key] > key

    def test_default_chutes_start_bigger_than_end(self):
        """
        Tests if the default chutes makes sens, in other words
        that the start is bigger than the end
        """
        b = cs.Board()
        for idx, key in enumerate(b.default_chutes):
            assert b.default_chutes[key] < key

    def test_goal_bigger_than_0(self):
        """Test if the goal is lager than 0"""
        b = cs.Board()
        assert b.goal > 0


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
    def test_move(self):
        """LazyPlayer can move."""
        b = cs.Board()
        p = cs.LazyPlayer(b)
        assert 0 == p.get_steps()
        assert 0 == p.get_position()
        p.move()
        assert 0 < p.get_position()
        assert 0 < p.get_steps()


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

    def test_single_game_with_seed(self):
        """single_game() returns non-negative number and class name"""
        s450 = cs.Simulation(player_field=[cs.Player], board=None, seed=450,
                             randomize_players=False)
        assert s450.single_game() == (11, 'Player')

    def test_winners_per_type_with_seed(self):
        """tests if winners_per_type() works with seed too"""
        s450 = cs.Simulation(
            player_field=[cs.Player, cs.LazyPlayer, cs.ResilientPlayer],
            board=None, seed=450,
            randomize_players=False)
        s450.run_simulation(7)
        assert s450.winners_per_type() == {
            'Player': 3, 'LazyPlayer': 1, 'ResilientPlayer': 3
        }

    def test_durations_per_type_with_seed(self):
        """tests if durations per type works with a seed too"""
        s450 = cs.Simulation(
            player_field=[cs.Player, cs.LazyPlayer, cs.ResilientPlayer],
            board=None, seed=450,
            randomize_players=False)
        s450.run_simulation(7)
        assert s450.durations_per_type() == {
            'Player': [11, 16, 16], 'LazyPlayer': [17],
            'ResilientPlayer': [12, 9, 4]
        }
