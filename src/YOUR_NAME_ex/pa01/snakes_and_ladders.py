import random
import time


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
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """

    players = {}
    for player in range(1, num_players + 1):
        players[player] = 0

    # Start game
    start = 1
    moves = 0
    time_start = time.time()
    while not start == 0:
        for player, current_pos in players.items():

            # Total moves
            moves += 1

            # Move player
            players[player] = move_player(player, current_pos)

            # Check win
            if players[player] > 89:
                time_end = time.time()
                start = 0
                return (time_end - time_start), moves


single_game(3)