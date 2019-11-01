n = 10


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]
    # 55 Modulus operator; gives the remainder of the left value divided by the right value:
    # 34 % 10 = 4, because 10*3=30, 10*4=40, so there is a remainder.


def squares_by_loop(n):
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)
    return squares


if __name__ == '__main__':
    if squares_by_comp(n) != squares_by_loop(n):
        print('ERROR!')
    if squares_by_comp(n) == squares_by_loop(n):  # Added this to confirm that it works for sure
        print('Sucsses!')
