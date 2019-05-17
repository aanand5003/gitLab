from Node import *

class Stack:
    def __init__(self):
        """Creates an empty stack"""
        self.top = None
        self.stack_size = 0

    def size(self):
        """Returns the size, i.e. the number
        of elements in the container."""
        return self.stack_size

    def is_empty(self):
        """Returns True if and only if the container is empty."""
        return self.size() == 0

    def is_full(self):
        """Returns True if and only if the container is full."""
        return False

    def push(self, item):
        """Places the given item at the top of the stack."""
        # here, thanks to the dummy node, we can always assume that top
        # refers to a Node, and not to None
        self.top = Node(item, self.top)
        self.stack_size += 1

    def pop(self):
        """Removes and returns the top element of the stack,
        or raises an Exception if there is none."""
        if self.is_empty():
            raise Exception("The stack is empty")
        item = self.top.item
        # removes a reference to this item,
        # helps with memory management and debugging
        self.top.item = None
        self.top = self.top.next
        self.stack_size -= 1
        return item

    def reset(self):
        """Removes all elements from the container."""
        while not self.is_empty():
            self.pop()
        assert (self.is_empty)