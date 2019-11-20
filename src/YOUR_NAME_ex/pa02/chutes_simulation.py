# -*- coding: utf-8 -*-

__author__ = 'Kaspar Akilles Lilja, Kevin Martin Lankut'
__email__ = 'kalilja@nmbu.no, kela@nombu.no'


import random


class Board:

    def __init__(self, chutes=None, ladders=None, goal=None):
        """
        :param chutes: can be entered as a custom list of chutes
        :param ladders: can be entered as a custom list of ladders
        :param goal: can be entered as a custom goal
        All these parameters have set standards, but can be altered.
        """
        if chutes is None:
            chutes = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                      (74, 12), (87, 70)]

        if ladders is None:
            ladders = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                       (65, 82), (68, 85)]

        self.chutes_ladders = dict(chutes + ladders)

        if goal is None:
            self.goal = 90
        else:
            self.goal = goal

    def goal_reached(self, position):
        """
        :param position: takes the position of a player
        :return: returns True if the player have reached goal
        """
        return position >= self.goal

    def position_adjustment(self, position):
        """
        :param position: takes the position of a player
        :return: returns if the player should move up or down a ladder/chute
        """
        for start, end in self.chutes_ladders.items():
            if position == start:
                return end - start
        return 0


class Player:

    def __init__(self, board):
        """
        :param board: takes a custom or standard board with chutes ladders and
        goal previously set.
        """
        self.position = 0
        self.board = board

    def move(self):
        """
        This function alters the position of the player, but does not return
        anything.
        """
        throw = random.randint(1, 6)
        self.position += throw
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):

    def __init__(self, board, extra_steps=1):
        """
        :param board: takes a custom or standard board with chutes ladders and
        goal previously set.
        :param extra_steps: is the extra number of steps the ResilientPlayer
        will move after going down a chute. Default = 1.
        """
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):
        """
        This function alters the position of the player, but does not return
        anything.
        """
        throw = random.randint(1, 6)
        self.position += throw

        while self.board.position_adjustment(self.position) < 0:
            self.position += self.board.position_adjustment(self.position)
            self.position += self.extra_steps
            throw2 = random.randint(1, 6)
            self.position += throw2

        if self.board.position_adjustment(self.position) > 0:
            self.position += self.board.position_adjustment(self.position)


class LazyPlayer(Player):

    def __init__(self, board, dropped_steps=1):
        """
        :param board: takes a custom or standard board with chutes ladders and
        goal previously set.
        :param dropped_steps: is the number of steps the LazyPlayer walks
         backwards after going up a ladder. Default = 1.
        """
        super().__init__(board)
        self.dropped_steps = dropped_steps

    def move(self):
        """
        This function alters the position of the player, but does not return
        anything, but if the result of moving is going backwards, then the move
        will simply not be executed.
        """
        throw = random.randint(1, 6)
        self.position += throw

        while self.board.position_adjustment(self.position) > 0:
            self.position += self.board.position_adjustment(self.position)
            throw2 = random.randint(1, 6)
            if throw2 > self.dropped_steps:
                self.position -= self.dropped_steps
                self.position += throw2

        if self.board.position_adjustment(self.position) < 0:
            self.position += self.board.position_adjustment(self.position)


class Simulation:

    def __init__(self, player_field, board=None, seed=None,
                 randomize_players=False):
        """
        :param player_field: is a list of all the different types of players
        participating in this game.
        :param board: takes a custom or standard board with chutes ladders and
        goal previously set.
        :param seed: is an alternative random seed
        :param randomize_players: is a boolean which if True, will randomize
        the player list.
        """
        self.player_field = player_field
        if board is None:
            self.board = Board()
        else:
            self.board = board
        self.seed = seed
        self.randomize_players = randomize_players
        self.victory_list = []
        self.winner_type = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}
        self.durations_type = {'Player': [], 'LazyPlayer': [],
                               'ResilientPlayer': []}
        self.players_type = {'Player': 0, 'LazyPlayer': 0,
                             'ResilientPlayer': 0}

    def single_game(self):
        """
        :return: a tuple consisting of the number of rounds required to finish
         the game, and which type of player that won.
        """
        if self.randomize_players:
            random.shuffle(self.player_field)
        random.seed(self.seed)
        player_lead = 0
        player_object_list = []
        player_moves = 0

        for i, player_i in enumerate(self.player_field):
            if player_i == Player:
                player_object_list.append(Player(self.board))
            elif player_i == ResilientPlayer:
                player_object_list.append(ResilientPlayer(self.board))
            elif player_i == LazyPlayer:
                player_object_list.append(LazyPlayer(self.board))
            else:
                raise TypeError(
                    '{0} is not a valid playertype'.format(player_i))

        while True:
            for i, player in enumerate(player_object_list):
                player.move()
                player_moves += 1
                if player.position > player_lead:
                    player_lead = player.position
                    if self.board.goal_reached(player_lead):
                        return tuple((int(player_moves),
                                      (self.player_field[i]).__name__))

    def run_simulation(self, n):
        """
        :param n: defines how many times single_game should be run, and saves
        the results to a list victory_list. run_simulation returns nothing.
        """

        for _ in range(n):
            self.victory_list.append(Simulation.single_game(self))

    def get_results(self):
        """
        :return: all results generated by run_simulation.
        """
        return self.victory_list

    def winners_per_type(self):
        """
        :return: dictionary mapping player types to the number of wins.
        """
        for i, player in self.victory_list[:1]:
            if self.winner_type[player] == 0:
                self.winner_type[player] = 1
            else:
                self.winner_type[player] += 1

        return self.winner_type

    def durations_per_type(self):
        """
        :return:  dictionary mapping player types to lists of game durations
        for that type.
        """
        for moves, player in self.victory_list:
            self.durations_type[player].append(moves)

        return self.durations_type

    def players_per_type(self):
        """
        :return: dictionary showing how many players of each type participate.
        """
        for player in self.player_field:
            self.players_type[str(player.__name__)] += 1

        return self.players_type
