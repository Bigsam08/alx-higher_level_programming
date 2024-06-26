#!/usr/bin/python3

""" check weight and score in my_list """


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    score = 0
    weight = 0
    for i in my_list:
        score += i[0] * i[1]
        weight += i[1]
    return score / weight
