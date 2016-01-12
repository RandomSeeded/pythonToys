# https://leetcode.com/problems/find-median-from-data-stream/

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# Examples:
# 
# [2,3,4] , the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
#     void addNum(int num) - Add a integer number from the data stream to the data structure.
#     double findMedian() - Return the median of all elements so far.
# 
# For example:
# 
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3) 
# findMedian() -> 2

# So, thing that jumps out at me is that we probably want a sorted data structure, due to our needing to be able to find the middle two values at any point in time. We can't just keep track of those two, because they may change over time. Add a bunch of larger values? What are the new mids? No frickin idea! Etc. So in order to do this properly, each value we add needs to at minimum know the one value next smaller, and the one value next larger, aka be sorted. 
# So what data structures could be good for that? Lists will be slow insertion and lookup (though we could improve lookup by keeping track of the two midpoints). 
# Sorted tree, probably.

# let's try out a 2-3 b tree
# Good idea, but this is going to run into serious issues when there's repeats. What can we do about that? Ewwwwwwww. Let's for now imagine there were no dups? That's not the best way to do this. Crap.

class Node:
    def __init__(self):
        self.left = None
        self.middle = None
        self.right = None
        self.value1 = None
        self.value2 = None
        self.value3 = None
        self.parent = None

    def inNode(self, value):
        if self.value1 == value or self.value2 == value or self.value3 == value:
            return True
        return False

    def isLeaf(self):
        return self.left == None
        
class MedianFinder:
    def __init__(self):
        self.root = Node()
        """
        Initialize your data structure here.
        """

    def search(self, value, currentNode):
        # Default to the root for starting searches
        if currentNode == None:
            currentNode = self.root

        # Leaf-node case
        if currentNode.isLeaf():
            # We will return the leaf where the node SHOULD go, even if it's not present in that node. This way we can use our search function for adding
            return currentNode

        # Recursive case on a 2-node
        elif currentNode.value2 == None:
            if currentNode.inNode(value):
                return currentNode
            elif value < currentNode.value1:
                return self.search(value, currentNode.left)
            else:
                return self.search(value, currentNode.right)
        
        # Recursive case on a 3-node
        else:
            if currentNode.inNode(value):
                return currentNode
            elif value < currentNode.value1:
                return self.search(value, currentNode.left)
            elif value > currentNode.value1 and value < currentNode.value2:
                return self.search(value, currentNode.middle)
            else:
                return self.search(value, currentNode.right)

    def addNum(self, num):
        leaf = self.search(num, None)

        # If there is only one element in the leaf, add here (2-node -> 3-node)
        if leaf.value2 == None:
            # Special case for root
            if leaf.value1 == None:
                leaf.value1 = num

            elif num < leaf.value1:
                leaf.value2 = leaf.value1
                leaf.value1 = num

            else:
                leaf.value2 = num

        # Otherwise, we now have a 4-node
        else:
            # Make this a 4-node
            leaf.value3 = num
            while leaf != None and leaf.value3 != None:
                # Place the 3rd num in the correct place
                if leaf.value3 < leaf.value1:
                    temp = leaf.value3
                    leaf.value3 = leaf.value2
                    leaf.value2 = leaf.value1
                    leaf.value1 = temp
                elif leaf.value3 < leaf.value2:
                    temp = leaf.value2
                    leaf.value2 = leaf.value3
                    leaf.value3 = temp

                # Move middle to the parent and split this node into two
                if leaf.parent == None:
                    leaf.parent = Node()
                    leaf.parent.value1 = leaf.value3
                elif leaf.parent.value2 == None:
                    leaf.parent.value2 = leaf.value3 # (note: this needs to be expanded, could be on left)
                else:
                    leaf.parent.value3 = leaf.value3



                # Point leaf to the parent, move up the chain
                leaf = leaf.parent
                
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.findMedian()

# YE OLDE CODE

# class Node:
#     def __repr__(self):
#         return str(self.data1)+","+str(self.data2)
# 
#     def __init__(self):
#         self.data1 = None
#         self.data2 = None
#         self.left = None
#         self.middle = None
#         self.right = None
#         self.parent = None
#         self.numData = 0
#         self.numChildren = 0
# 
#     def inNode(self, value):
#         if self.data1 == value or self.data2 == value:
#             return True
#         return False
#     
#     def isLeaf(self):
#         return self.numChildren == 0
# 
# 
# class MedianFinder:
#     def __repr__(self):
#         return str(self.root)
# 
#     def __init__(self):
#         self.root = Node()
#         """
#         Initialize your data structure here.
#         """
# 
#     def search(self, value, currentNode):
#         # Default to the root for starting searches
#         if currentNode == None:
#             currentNode = self.root
# 
#         # Leaf-node case
#         if currentNode.isLeaf():
#             # We will return the leaf where the node SHOULD go, even if it's not present in that node. This way we can use our search function for adding
#             return currentNode
# 
#         # Recursive case on a 2-node
#         elif self.numChildren == 2:
#             if currentNode.inNode(value):
#                 return currentNode
#             elif value < currentNode.data1:
#                 return self.search(value, currentNode.left)
#             else:
#                 return self.search(value, currentNode.right)
#         
#         # Recursive case on a 3-node
#         else:
#             if currentNode.inNode(value):
#                 return currentNode
#             elif value < currentNode.data1:
#                 return self.search(value, currentNode.left)
#             elif value > currentNode.data1 and value < currentNode.data2:
#                 return self.search(value, currentNode.middle)
#             else:
#                 return self.search(value, currentNode.right)
# 
#     def addNum(self, num):
#         leaf = self.search(num, None)
# 
#         # If there is only one element in the leaf, add here (2-node -> 3-node)
#         if leaf.numData < 2:
#             # Special case for root
#             if leaf.data1 == None:
#                 leaf.data1 = num
# 
#             elif num < leaf.data1:
#                 leaf.data2 = leaf.data1
#                 leaf.data1 = num
# 
#             else:
#                 leaf.data2 = num
# 
#             leaf.numData+=1
# 
#         # Otherwise, we now have a 4-node
#         else:
#             leaf.numData += 1
#             while leaf.numData == 3:
#             # Assign the 'middle' node to the parent
#                 if num < leaf.data1:
#                     middleData = leaf.data1
#                     leaf.data1 = num
#                 elif num > leaf.data2:
#                     middleData = leaf.data2
#                     leaf.data2 = num
#                 else:
#                     middleData = num
# 
#         """
#         Adds a num into the data structure.
#         :type num: int
#         :rtype: void
#         """
#         
# 
#     def findMedian(self):
#         """
#         Returns the median of current data stream
#         :rtype: float
#         """
