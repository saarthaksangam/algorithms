"""
Problem: Find Loop
Problem Statement: https://www.algoexpert.io/questions/Find%20Loop
NTID: NT-100
Category: Linked Lists
Difficulty: Hard
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/08/2022
"""


class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None
        

# O(n) time | O(1) space
def findLoop(head):
    """
    The findLoop function finds the first node of a loop in a linked list.
       It takes as input the head of a linked list and returns the first node
       in the loop.

    :param head: Keep track of the current node
    :return: The node at which the loop starts
    :doc-author: Trelent
    """
    slow = head.next  # slow pointer
    fast = head.next.next  # fast pointer - skips 1 node
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    # when fast and slow meet
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
