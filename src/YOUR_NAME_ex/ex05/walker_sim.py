# -*- coding: utf-8 -*-
import random

__author__ = 'Kevin Martin Lankut'
__email__ = 'kela@nmbu.no'


class Walker:
    """
    class simulating movement of a person in a one dimensional world from start to home
    """

    def __init__(self, start, home):
        """
        :param start: initial position of the walker
        :param home: position of the walker's home
        """
        self.start = start
        self.home = home
        self.steps = 0

    def get_position(self):
        """Returns current position."""
        return self.start

    def get_steps(self):
        """Returns number of steps taken by walker."""
        return self.steps

    def is_at_home(self):
        """Returns True if walker is at home position."""
        if self.start is self.home:
            return True
        return False

    def move(self):
        """
        Change coordinate by +1 or -1 with equal probability.
        """
        direction = random.randint(0, 1)
        if direction == 0:
            self.start -= 1
        elif direction == 1:
            self.start += 1
        self.steps += 1


class Simulation:
    """
    class simulating the whole journey from start to home
    """

    def __init__(self, start, home, seed):
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
        """
        self.start = start
        self.home = home
        self.seed = seed

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        random.seed(self.seed)
        w = Walker(self.start, self.home)
        position = w.get_position()
        while position != self.home:
            w.move()
            position = w.get_position()
        return w.get_steps()

    def run_simulation(self, num_walks):
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
            simulation = self.single_walk()
            total_steps.append(simulation)
        return total_steps


if __name__ == "__main__":
    for _ in range(0, 2):
        S1 = Simulation(0, 10, 12345)
        print(S1.run_simulation(20))
    S2 = Simulation(0, 10, 54321)
    print(S2.run_simulation(20))

    for i in range(0, 2):
        S3 = Simulation(10, 0, 12345)
        print(S3.run_simulation(20))
    S4 = Simulation(10, 0, 54321)
    print(S4.run_simulation(20))
