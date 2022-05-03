"""
Problem: Permutations
Problem Statement: https://www.algoexpert.io/questions/Permutations
NTID: NT-114
Category: Recursions
Difficulty: Medium
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/02/2022
"""


# Time Complexity: O(n*n!) | Space Complexity: O(n*n!) space
def getPermutations(array):
    """
    The getPermutations function takes an array of integers and returns a list containing all permutations of those
    numbers. For example, if the input is [2,3], then the function will return [[2,3],[3,2]].


    :param array: Store the current permutation that is being built
    :return: An array of all possible permutations
    :doc-author: Trelent
    """
    # Write your code here.
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, arr, permutations):
    """
    The permutationsHelper function takes in 3 parameters: i, arr, and permutations.
    The function will then iterate through the array from index i to the end of the array.
    For each iteration of this loop, it will swap arr[i] with every element after it (from index i to end).
    After this is done for all elements in range(i), we append a copy of our current state of arr into permutations.

    :param i: Keep track of the current index in the array that we are swapping
    :param arr: Store the current permutation
    :param permutations: Store the permutations as they are generated
    :return: A list of all permutations of a given array
    :doc-author: Trelent
    """
    if i == len(arr) - 1:
        permutations.append(arr[:])
    else:
        for j in range(i, len(arr)):
            swap(arr, i, j)
            permutationsHelper(i + 1, arr, permutations)
            swap(arr, i, j)


def swap(arr, i, j):
    """
    The swap function swaps the values of two variables.

    Parameters:
        arr (list): The list to swap elements in.

        i (int): The index of the first element to be swapped.

        j (int): The index of the second element to be swapped.


    :param arr: Store the list of numbers
    :param i: Define the index of the first element in the array
    :param j: Indicate the index of the element that will be swapped with i
    :return: The value of the array at index i
    :doc-author: Trelent
    """
    arr[i], arr[j] = arr[j], arr[i]
