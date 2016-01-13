class Node:
    def __repr__(self):
        return str(self.values) + " with children: "+str(self.children)
    def __init__(self, isLeaf = True, numElements = 0, parent = None):
        self.values = []
        self.children = []

        self.isLeaf = isLeaf
        self.numElements = numElements
        self.parent = parent

class BTree:
    def __repr__(self):
        return str(self.root)
    def __init__(self):
        self.root = Node()
        self.n = 0

    def insert(self, val):
        pass


myTree = BTree()

myTree.insert(5)
print(myTree)

