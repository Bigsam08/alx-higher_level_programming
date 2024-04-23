#!/usr/bin/python3
""" Replicates Pascal's Triangle in list form """


def pascal_triangle(n):
    """ creates Pascal's Triangle
    """
    lists = []
    if n <= 0:
        return lists
    for si in range(n):
        lst = []
        for i in range(si + 1):
            if i == 0 or i == si:
                val = 1
            else:
                val = lists[si - 1][i - 1] + lists[si - 1][i]
            lst.append(val)
        lists.append(lst)
    return lists
