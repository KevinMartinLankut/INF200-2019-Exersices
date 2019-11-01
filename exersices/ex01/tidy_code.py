from random import randint as r

__author__ = ''
__email__ = '@nmbu.no'


def your_guess():
    c = 0
    while c < 1:  # This while loop prevents negative numbers and strings. It forces you to answer positive numbers.
        c = int(input('Your guess between 1-10: '))
    return c


def random_nr():
    return r(1, 6) + r(1, 6)  # generates a random number from 1-5 twice, and then adds them togheter


def check(f, g):
    return f == g  # Checks if the two numbers are equal each other


if __name__ == '__main__':

    result = False
    tries = 3  # Amount of tries you have to guess
    random = random_nr()

    while not result and tries > 0:  # While result and tries are not bigger than 0
        guess = your_guess()
        result = check(random, guess)  # hecks if your guess and random generated number is the same
        if not result:  # If the numbers aren't the same
            print('Wrong, try again!')
            tries -= 1  # A try is taken away from total amount of tries

    if tries > 0:  # If you have tries left
        print('You won {} points.'.format(tries))  # you won the amount of tries left in points
    else:
        print('You lost. Correct answer: {}.'.format(random))  # Otherwise you lost. Show the randomly generated number
