"""
Problem: Number of Binary Tree Topologies
Problem Statement: https://www.algoexpert.io/questions/Number%20Of%20Binary%20Tree%20Topologies
NTID: NT-121
Category: Recursions
Difficulty: Extreme
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/07/2022
"""


# Naïve Recursive Solution -> O(n*(2n)!/(n!(n+1)!)) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    if n == 0:
        return 1
    numberOfTreeTopologies = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - leftTreeSize - 1  # n - 1 because we always have a root
        numberOfTreeTopologies += numberOfBinaryTreeTopologies(leftTreeSize) * numberOfBinaryTreeTopologies(
            rightTreeSize)

    return numberOfTreeTopologies


# Optimized Recursive Solution -> O9n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n, cache={0: 1}):
    # Write your code here.
    if n in cache:
        return cache[n]
    numberOfTreeTopologies = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - leftTreeSize - 1  # n - 1 because we always have a root
        numberOfTreeTopologies += numberOfBinaryTreeTopologies(leftTreeSize, cache) * numberOfBinaryTreeTopologies(
            rightTreeSize, cache)
    cache[n] = numberOfTreeTopologies
    return numberOfTreeTopologies


# Optimized Iterative Solution -> O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    cache = [1]
    for m in range(1, n + 1):
        numberOfTreeTopologies = 0
        for leftTreeSize in range(m):
            rightTreeSize = m - leftTreeSize - 1  # m - 1 because we always have a root
            numberOfTreeTopologies += cache[leftTreeSize] * cache[rightTreeSize]
        cache.append(numberOfTreeTopologies)
    return cache[-1]
