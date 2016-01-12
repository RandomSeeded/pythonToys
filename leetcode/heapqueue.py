# Simplest version: using an array to represent a binary tree
import math
class Heap:
    def __repr__(self):
        return str(self.storage)

    def __init__(self):
        self.storage = []

    def fixHeap(self, position):
        # child of 0: 1 and 2
        # child of 1: 3 and 4
        # child of 2: 5 and 6
        parent = math.floor((position - 1) / 2)
        if position > 0 and self.storage[position] < self.storage[parent]:
            temp = self.storage[position]
            self.storage[position] = self.storage[parent]
            self.storage[parent] = temp
            self.fixHeap(parent)

    def push(self, value):
        self.storage.append(value)
        self.fixHeap(len(self.storage)-1)

    def pop(self):
        result = self.storage[0]
        self.storage[0] = self.storage[len(self.storage)-1]
        del self.storage[len(self.storage)-1]
        return result


# testing
myH = Heap()
myH.push(4)
print(myH)
myH.push(2)
print(myH)
myH.push(3)
print(myH)
myH.push(1)
print(myH)
myH.push(7)
print(myH)
myH.push(6)
print(myH)
myH.push(-1)
print(myH)
myH.push(0)
print(myH)
myH.push(5)
print(myH)
