"""
Problem: Find Closest Value in BST
Problem Statement: https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST
NTID: NT-26
Category: Binary Search Trees
Difficulty: Easy
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/01/2022
"""


def findClosestValueInBst(tree, target):
    return findClosestValueInBSTHelperRecursive(tree, target, float('inf'))


# Recursive Solution
'''
Average Time Complexity: O(log(n))
Average Space Complexity: O(1)

Worst Time Complexity: O(n)
Worst Space Complexity: O(n)
'''
def findClosestValueInBSTHelperRecursive(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelperRecursive(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelperRecursive(tree.right, target, closest)
    else:
        return closest


# Iterative Solution
'''
Average Time Complexity: O(log(n))
Average Space Complexity: O(1)

Worst Time Complexity: O(n)
Worst Space Complexity: O(1)
'''
def findClosestValueInBSTHelperIterative(tree, target, closest=float('inf')):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
