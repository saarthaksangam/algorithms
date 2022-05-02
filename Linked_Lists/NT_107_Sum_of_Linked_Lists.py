# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(n, m)) time | O(max(n, m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    """
    The sumOfLinkedLists function takes two linked lists as arguments.
    It creates a new linked list whose head is the sum of the values in each node of both input lists.
    The function returns a reference to this newly created list.

    :param linkedListOne: Keep track of the current node in linkedListOne
    :param linkedListTwo: Keep track of the current node in linkedListTwo
    :return: The head of the new linked list
    :doc-author: Trelent
    """
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
