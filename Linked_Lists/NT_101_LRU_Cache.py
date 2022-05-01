"""
Problem: LRU Cache
Problem Statement: https://www.algoexpert.io/questions/LRU%20Cache
NTID: NT-101
Category: Linked Lists
Difficulty: Extreme
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/01/2022
"""


class LRUCache:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.currentSize = 0
        self.listofMostRecent = DoublyLinkedList()

        
    def insertKeyValuePair(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.removeLeastRecentKey()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKeyValuePair(key, value)

        self.updateMostRecent(self.cache[key])

        
    def getValueFromKey(self, key: int) -> int:
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    
    def getMostRecentKey(self) -> int:
       if self.listofMostRecent.head is None:
            return None
        return self.listofMostRecent.head.key

    
    def replaceKeyValuePair(self, key: int, value: int) -> None:
        if key not in self.cache:
            raise Exception("Key not found in cache!")  # sanity check
        else:
            self.cache[key].value = value

            
    def removeLeastRecentKey(self) -> None:
       keyToRemove = self.listofMostRecent.tail.key
        self.listofMostRecent.removeTail()
        del self.cache[keyToRemove]

  
    def updateMostRecent(self, node) -> None:
        self.listofMostRecent.setHeadTo(node)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        
    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node

        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail

        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

            
    def removeTail(self):      
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):       
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
