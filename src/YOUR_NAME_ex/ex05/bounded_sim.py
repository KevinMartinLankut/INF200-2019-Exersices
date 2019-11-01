# -*- coding: utf-8 -*-

__author__ = 'Kevin Martin Lankut'
__email__ = 'kela@nmbu.no'

from walker_sim import Walker, Simulation
import random


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

    def bounded_move(self):
        if self.start != self.left_limit and self.start != self.right_limit:
            Walker.move(self)
        elif self.start == self.left_limit:
            self.start += 1
            self.steps += 1
        elif self.start == self.right_limit:
            self.start -= 1
            self.steps += 1

        """'If the random generator decides that the walker should move beyond
        a limit, the move is simply not executed.' I can't think of any way
        to actually execute move(), and check what the random generator
        generates to then stop it before it goes on to moving the walker
        and adding steps. I also don't see the point of adding a new generator
        to then see if it moves or not, considering that at the end you don't
        want to see amount of *potential* moves, but amount of *steps*, meaning
        even if the generator goes past a limit, it doesn't count it, so might
        as well just start moving in the right direction because eventually
        it will do that."""


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        self.seed = seed
        self.left_limit = left_limit
        self.right_limit = right_limit
    
    def bounded_single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        random.seed(self.seed)
        bw = BoundedWalker(self.start, self.home, self.left_limit, self.right_limit)
        position = bw.get_position()
        while position != self.home:
            bw.bounded_move()
            position = bw.get_position()
        return bw.get_steps()

    def run_bounded_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        total_steps = []
        for _ in range(0, num_walks):
            simulation = self.bounded_single_walk()
            total_steps.append(simulation)
        return total_steps


if __name__ == "__main__":
    left = [0, -10, -100, -1000, -10000]
    for i in left:
        bs = BoundedSimulation(0, 20, 12345, i, 20)
        bs_results = bs.run_bounded_simulation(20)
        print('Left boundary: {0}. Total steps: {1}'.format(i, bs_results))
