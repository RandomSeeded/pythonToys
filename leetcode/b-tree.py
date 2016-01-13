class Node:
    def __repr__(self):
        return str(self.values) + " with children: "+ str(self.children)

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

    def search(self, val, currentNode = None):
        """
        Returns the node where a value should be placed
        :rtype: Node
        """
        if currentNode == None:
            currentNode = self.root

        if currentNode.isLeaf or val in currentNode:
            return currentNode
        else:
            for i in range(len(self.values)):
                if val < self.values[i]:
                    return self.search(val, self.children[i])
            return self.search(val, self.children[i])

    def insert(self, val):
        location = self.search(val)
        if location.numElements < 3:
            location.values.append(val)
            location.numElements+=1
        elif location.parent == None:
            pass
        elif location.parent.numElements < 3:
            pass
        else:
            pass


myTree = BTree()

myTree.insert(5)
myTree.insert(4)
myTree.insert(3)
myTree.insert(2)
myTree.insert(1)
print(myTree)

