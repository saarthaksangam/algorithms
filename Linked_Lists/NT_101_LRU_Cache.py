"""
Problem: LRU Cache
Problem Statement: https://www.algoexpert.io/questions/LRU%20Cache
NTID: NT_101
Category: Linked Lists
Difficulty: Extreme
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/01/2022
"""


class LRUCache:
    def __init__(self, maxSize: int):
        """
        The __init__ function initializes the class with a maxSize parameter.
        The cache is initialized as an empty dictionary. The current size of the cache is set to 0.

        :param self: Refer to the instance of the class
        :param maxSize:int: Set the maximum size of the cache
        :return: The cache object
        :doc-author: Trelent
        """
        self.maxSize = maxSize or 1
        self.cache = {}
        self.currentSize = 0
        self.listofMostRecent = DoublyLinkedList()

    def insertKeyValuePair(self, key: int, value: int) -> None:
        """
        The insertKeyValuePair function inserts a key-value pair into the hash table.
           If the key already exists in the hash table, then its value is overwritten with
           the new value. Otherwise, if it does not exist in the hash table, then it is added to
           end of linked list that corresponds to its bucket.

        :param self: Refer to the object itself
        :param key:int: Specify the key of the key-value pair to be inserted
        :param value:int: Store the value of the key-value pair to be inserted
        :return: None
        :doc-author: Trelent
        """
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
        """
        The getValueFromKey function takes in a key and returns the value associated with that key. If the key is not present, it returns None.


        :param self: Access the class variables
        :param key:int: Access the value of a particular key in the cache
        :return: The value of the key that is passed in
        :doc-author: Trelent
        """
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self) -> int:
        """
        The getMostRecentKey function returns the most recent key added to the cache.
        If no keys have been added, it returns None.

        :param self: Refer to the current object
        :return: The most recent key
        :doc-author: Trelent
        """

        if self.listofMostRecent.head is None:
            return None
        return self.listofMostRecent.head.key

    def replaceKeyValuePair(self, key: int, value: int) -> None:
        """
        The replaceKeyValuePair function replaces the value associated with a key in the cache.
        If the key is not found, it raises an exception. If it is found, then its value will be replaced by
        the new one.

        :param self: Refer to the object itself
        :param key:int: Specify the key of the element to be replaced
        :param value:int: Replace the value of a key in the cache
        :return: None
        :doc-author: Trelent
        """

        if key not in self.cache:
            raise Exception("Key not found in cache!")  # sanity check
        else:
            self.cache[key].value = value

    def removeLeastRecentKey(self) -> None:
        """
        The removeLeastRecentKey function removes the least recently used key from the hashmap.
        It does this by removing the tail of listofMostRecent, which is a doubly linked list.
        The function returns None.

        :param self: Refer to the object itself
        :return: None
        :doc-author: Trelent
        """
        keyToRemove = self.listofMostRecent.tail.key
        self.listofMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node) -> None:
        """
        The updateMostRecent function updates the mostRecent pointer to point to the given node.

        :param self: Refer to the object of the class
        :param node:DoublyLinkedListNode: Update the most recent node
        :return: The node that was updated
        :doc-author: Trelent
        """
        self.listofMostRecent.setHeadTo(node)


class DoublyLinkedList:
    def __init__(self):
        """
        The __init__ function is called automatically every time the class is being used to create a new object. The
        first argument of every class method, including init, is always a reference to the current instance of the
        class. By convention, this argument is always named self. In the init method we assign self.head = None and
        self.tail = None.

        :param self: Refer to the instance of the class
        :return: The object that we have created
        :doc-author: Trelent
        """
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        """
        The setHeadTo function takes a node as an argument and sets the head of the linked list to that node. If the
        head is already set to that node, then nothing happens. If there are no nodes in this linked list,
        then it simply sets the head and tail of this linked list to be equal to that one node. If there is only one
        node in this linked list, then it removes all bindings from both sides of said singleton-linked-list (the
        tail) and makes its next pointer point back towards its previous pointer which points towards None (null).
        Finally, if there are more than two nodes in this LinkedList class instance's object variables (head and
        tail), then we check if the current value for our tail variable equals our inputted parameter for 'node'. If
        so, we remove said binding by calling on our removeTail function; otherwise we do nothing because either way
        these two pointers will still be pointing at each other.

        :param self: Access the data inside the class
        :param node: Set the head of the linked list to that node
        :return: Nothing
        :doc-author: Trelent
        """

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
        """
        The removeTail function removes the last node in the linked list.
        If there is only one node, it removes that single node.
        If there are no nodes, it does nothing.

        :param self: Refer to the instance of the class
        :return: The head of the linked list
        :doc-author: Trelent
        """

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
        """
        The __init__ function is called when an instance of the class is created.
        The __init__ function is usually where you will initialize all variables for that class.

        :param self: Refer to the instance of the class
        :param key: Store the key of the node
        :param value: Store the value of the key-value pair
        :return: The object of the class
        :doc-author: Trelent
        """

        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        """
        The removeBindings function removes the current binding from the list of bindings.
        It does this by setting the previous and next pointers to None, which effectively removes it from the list.

        :param self: Refer to the current instance of the class
        :return: The value of self
        :doc-author: Trelent
        """

        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
