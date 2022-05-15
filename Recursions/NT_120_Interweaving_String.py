"""
Problem: Interweaving String
Problem Statement: https://www.algoexpert.io/questions/Interweaving%20String
NTID: NT-120
Category: Recursion
Difficulty: Hard
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/15/2022
"""


# O(2 ^ (n+m)) time | O(n+m) space without cache
# O(nm) time | O(nm) space with cache
def interweavingStrings(one, two, three):
    """
    The interweavingStrings function takes three strings, one and two which are the first
    and second string respectively, and a third string three. The function will return True if
    three can be formed by interweaving the characters of one and two in a way that maintains
    the order of these characters. If this is not possible then it will return False.

    :param one: Takes in the first string
    :param two: Takes in the second string
    :param three: Takes in the third string that we need to match
    :return: True if the strings one and two can be interwoven into string three, otherwise it returns false
    :doc-author: Trelent
    """
    if len(one) + len(two) != len(three):
        return False
    cache = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]
    return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, i, j, cache):
    """
    The areInterwoven function takes three strings, one and two and three.
    It also takes an index i for the first string, and an index j for the second string.
    The function returns True if there is a way to interweave the two strings starting at
    index i of string one, and index j of string two such that they match with third given
    string three. The function returns False otherwise.

    :param one: Takes in the first string
    :param two: Takes in the second string
    :param three: Takes in the third string that we need to match
    :param i: Keep track of the index in the first string
    :param j: Keep track of the current index in the second string
    :param cache: Store the results of subproblems so that they can be reused later
    :return: True if the strings one and two can be interwoven into string three
    :doc-author: Trelent
    """
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False
