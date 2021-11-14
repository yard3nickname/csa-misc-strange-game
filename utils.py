from itertools import combinations


def comb3(s):
    return combinations(s, 3)


def is_any_comb3_sum_eq15(s):
    return any(filter(lambda x: (sum(x) == 15), comb3(s)))
