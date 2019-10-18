# -*- coding: utf-8 -*-

__authors__ = 'Kaspar Akilles Lilja, Kevin Martin Lankut'
__emails__ = 'kalilja@nmbu.no, kela@nmbu.no'

"""
Source:
https://codereview.stackexchange.com/questions/176586/snakes-and-ladders-game
"""

import random
import statistics


def move_player(player, current_pos):
    snake_squares = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    ladder_squares = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}

    throw = random.randint(1, 6)
    next_pos = current_pos + throw
    if next_pos in snake_squares:
        next_pos = snake_squares[next_pos]
    elif next_pos in ladder_squares:
        next_pos = ladder_squares[next_pos]
    return next_pos


def single_game(num_players):
    players = {}
    for player in range(1, num_players + 1):
        players[player] = 0

    # Start game
    start = 1
    moves = 0
    while not start == 0:
        for player, current_pos in players.items():

            # Total moves
            moves += 1

            # Move player
            players[player] = move_player(player, current_pos)

            # Check win
            if players[player] > 89:
                start = 0
                return moves


def multiple_games(num_games, num_players):
    total_games = []
    for i in range(1, num_games + 1):
        games = single_game(num_players)
        total_games.append(games)
    return total_games


def multi_game_experiment(num_games, num_players, seed):
    random.seed(seed)
    return multiple_games(num_games, num_players)


if __name__ == "__main__":
    result = multi_game_experiment(100, 4, 89)
    result.sort()
    print(result[0], result[99])
    print(statistics.median(result))
    print(statistics.mean(result), statistics.stdev(result))
