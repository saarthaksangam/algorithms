"""
Problem: Sum of Linked Lists
Problem Statement: https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
NTID: NT-107
Category: Linked Lists
Difficulty: Medium
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/02/2022
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(n, m)) time | O(max(n, m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLLHead = LinkedList(0)
    currNode = newLLHead
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0

        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currNode.next = newNode
        currNode = newNode

        carry = sumOfValues // 10

        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None
    return newLLHead.next
