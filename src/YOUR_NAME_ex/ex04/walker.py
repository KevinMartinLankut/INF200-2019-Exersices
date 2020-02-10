# -*- coding: utf-8 -*-
import random

__author__ = 'Kevin Martin Lankut'
__email__ = 'kela@nmbu.no'


class Walker:
    def __init__(self, x0, h):
        self.x0 = x0
        self.h = h
        self.steps = 0
        self.goal = 0

    def is_at_home(self):
        if self.x0 == self.h:
            self.goal = 1

    def move(self):
        if self.goal == 0:
            self.steps += 1
            direction = random.randint(0, 1)
            if direction == 0:
                self.x0 -= 1
            elif direction == 1:
                self.x0 += 1
        self.is_at_home()

    def get_position(self):
        return self.x0

    def get_steps(self):
        return self.steps


def walker_simulator(x0, h):
    w = Walker(x0, h)
    walking = w.goal
    while walking == 0:
        w.move()
        walking = w.goal
    return w.get_steps()


def five_walker_simulations(x0, h):
    distance = h - x0
    total_steps = []
    for i in range(0, 6):
        simulation = walker_simulator(x0, h)
        total_steps.append(simulation)
    return print('Distance: {0} -> Total steps in each simulation: {1}'.format(distance, total_steps))


if __name__ == "__main__":
    five_walker_simulations(0, 1)
    five_walker_simulations(0, 2)
    five_walker_simulations(0, 5)
    five_walker_simulations(0, 10)
    five_walker_simulations(0, 20)
    five_walker_simulations(0, 50)
    five_walker_simulations(0, 100)
