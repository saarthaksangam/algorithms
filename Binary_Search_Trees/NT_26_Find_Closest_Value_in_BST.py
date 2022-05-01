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
    """
    The findClosestValueInBst function finds the closest value to a target value in a BST.
       The function takes in two parameters: tree and target, both of which are integers.
       The function returns an integer.

    :param tree: Keep track of the tree that is being searched
    :param target: Store the value of the node that is being searched for
    :return: The closest value to the target
    :doc-author: Trelent
    """
    # Write your code here.
    return findClosestValueInBSTHelperRecursive(tree, target, float('inf'))


# Recursive Solution
'''
Average Time Complexity: O(log(n))
Average Space Complexity: O(1)

Worst Time Complexity: O(n)
Worst Space Complexity: O(n)
'''


def findClosestValueInBSTHelperRecursive(tree, target, closest):
    """
    The findClosestValueInBSTHelperRecursive function takes in a BST and a target value. It then traverses the tree
    recursively and returns the closest value to that target

    :param tree: Keep track of the current node
    :param target: Store the value of the node that is being searched for
    :param closest: Keep track of the closest value so far
    :return: The closest value to the target
    :doc-author: Trelent
    """
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
    """
    The findClosestValueInBSTHelperIterative function takes in a BST and a target value,
    and returns the closest value to that target value contained in the BST. The function
    uses an iterative approach to find this closest value.

    :param tree: Keep track of the current node
    :param target: Store the value of the node that is being searched for
    :param closest=float('inf'): Keep track of the closest value so far
    :return: The closest value in the bst
    :doc-author: Trelent
    """
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
