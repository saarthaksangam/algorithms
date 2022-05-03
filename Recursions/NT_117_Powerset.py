"""
Problem: Powerset
Problem Statement: https://www.algoexpert.io/questions/Powerset
NTID: NT-117
Category: Recursions
Difficulty: Medium
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/03/2022
"""


# Iterative solution
# Time Complexity:  O(n*2^n)| Space Complexity: O(n*2^n)
def powerset(array):
    """
    The powerset function returns all the possible subsets of an input set.
    For example, powerset([0, 1]) returns [[], [0], [0, 1]].
    The function should be able to handle an undefined amount of inputs.


    :param array: Keep track of the subsets that we have already generated
    :return: All the possible subsets of an array
    :doc-author: Trelent
    """
    # Write your code here.
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [element])
    return subsets


# Recursive solution
# Time Complexity:  O(n*2^n)| Space Complexity: O(n*2^n)
def powerset(array, idx=None):
    """
    The powerset function returns all the possible subsets of an array.
    For example, powerset([0, 1]) returns [[], [0], [0, 1]].
    The function accepts two parameters: a list and an optional index. If no index is provided, the function will return all possible subsets of the given list starting from the first element up to and including the last element in that list.

    :param array: Store the current subset
    :param idx=None: Keep track of the index in the array
    :return: The powerset of the input array
    :doc-author: Trelent
    """
    # Write your code here.
    # array -> [1, 2, 3, 4]
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    ele = array[idx]
    # ele = 4
    subsets = powerset(array, idx - 1)
    # subsets = powerset(array, 2) => powerset([1, 2, 3])
    for i in range(len(subsets)):
        currSubset = subsets[i]
        subsets.append(currSubset + [ele])
    return subsets
