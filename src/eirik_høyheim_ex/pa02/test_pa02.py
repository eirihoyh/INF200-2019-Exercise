# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim, Meenbet A.Delele"
__email__ = "eirihoyh@nmbu.no, mesenbea@nmbu.no"

import chutes_simulation as cs

import pytest


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