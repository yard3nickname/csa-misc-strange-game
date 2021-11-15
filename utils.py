from itertools import combinations


def generate_comb3(s):
    return combinations(s, 3)


def is_match_game_object(s):
    return any(filter(lambda x: (sum(x) == 15), generate_comb3(s)))


def generate_magic_square(n):
    # 2-D array with all
    # slots set to 0
    magic_square = [[0 for x in range(n)] for y in range(n)]

    # initialize position of 1
    i = n / 2
    j = n - 1

    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:

            # next number goes out of
            # right side of square
            if j == n:
                j = 0

            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1

        if magic_square[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magic_square[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1  # 1st condition

    return magic_square
