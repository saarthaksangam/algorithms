"""
Problem: Two Number Sum
Problem Statement: https://www.algoexpert.io/questions/Two%20Number%20Sum
NTID: NT-1
Category: Arrays
Difficulty: Easy
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/08/2022
"""


# Naive Solution -> O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    """
    The twoNumberSum function takes in an array and a target sum. It then iterates through the array,
    and for each element it checks if the difference between that element and the target sum is also in
    the array. If so, it returns both elements as a list.

    :param array: Store the numbers in a list
    :param targetSum: Find the sum of two numbers that equal to it
    :return: A list of the two numbers that sum to targetsum
    :doc-author: Trelent
    """
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


# Optimized Solution using Hashmap -> O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []


# More optimized solution -> O(nlogn) time | O(1) space
def twoNumberSum(array, targetSum):
    array = sorted(array)
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []
