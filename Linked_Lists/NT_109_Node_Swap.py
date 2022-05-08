"""
Problem: Node Swap
Problem Statement: https://www.algoexpert.io/questions/Node%20Swap
NTID: NT-109
Category: Linked Lists
Difficulty: Extreme
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/07/2022
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Recursive solution
# O(n) time | O(n) space
def nodeSwap(head):
    """
    The nodeSwap function takes a linked list and swaps the next node with the previous node.
    For example, if we have a linked list: 1 -> 2 -> 3 ->   4
    The function will return: 2 -> 1 -> 4-> 3

    :param head: Keep track of the "new"  head of the linked list
    :return: The head of the linked list
    :doc-author: Trelent
    """
    # Write your code here.
    if head or head.next:
        return head

    nextNode = head.next
    head.next = nodeSwap(head.next.next)
    nextNode.next = head
    return nextNode


# Iterative solution
# O(n) time | O(1) space
def nodeSwap(head):
    """
    The nodeSwap function swaps every two nodes in the linked list.
    The function takes a head node as an argument and returns the new head node of the swapped list.

    :param head: Keep track of the head node
    :return: The head of the linked list
    :doc-author: Trelent
    """
    # Write your code here.
    tempNode = LinkedList(0)
    tempNode.next = head

    prevNode = tempNode
    while prevNode.next and prevNode.next.next:
        firstNode = prevNode.next
        secondNode = prevNode.next.next

        firstNode.next = secondNode.next
        secondNode.next = firstNode
        prevNode.next = secondNode
        prevNode = firstNode
    return tempNode.next
