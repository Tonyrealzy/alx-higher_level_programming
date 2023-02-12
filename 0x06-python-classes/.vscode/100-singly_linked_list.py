#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        if type(value) != int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def next_node(self, value):
        self.__next_node = value
        if type(value) != Node or value != None:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def print_list(self):
        temp = self.__head
        while temp:
            print(temp.data)
            temp = temp.next
linked_list = SinglyLinkedList()
linked_list.head = Node(1)
position = Node(n)
n = 2
n += 1

linked_list.head.next = second
while n:
    second.next = position

    def sorted_insert(self, value):
        s