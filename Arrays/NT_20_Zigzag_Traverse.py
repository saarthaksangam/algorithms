"""
Problem: Zigzag Traverse
Problem Statement: https://www.algoexpert.io/questions/Zigzag%20Traverse
NTID: NT-20
Category: Arrays
Difficulty: Hard
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/08/2022
"""


# O(n) time | O(n) space
def zigzagTraverse(arr):
    height = len(arr) - 1
    width = len(arr[0]) - 1
    result = []
    row, col = 0, 0
    goingDown = True
    while not (row < 0 or row > height or col < 0 or col > width):
        result.append(arr[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result
