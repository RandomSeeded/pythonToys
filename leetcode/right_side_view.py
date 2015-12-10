# https://leetcode.com/problems/binary-tree-right-side-view/
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# 
# For example:
# Given the following binary tree,
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# 
# You should return [1, 3, 4]. 


# IDEA: from root, we go right continually.
# If we can't go right, we go left (and then go right continually)
# ISSUE: what happens if we can go right a wee bit, but eventually need to go left and then right?
# IDEA: we just just store for each depth as we go along. So we depth first search from the right, but we'll eventually check every node
# If we have something already in storage for that depth, we don't overwrite
# ALT: we actually just depth-first search from the left, and we ALWAYS overwrite

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        def depthFirstSearch(node, depth):
            if node == None:
                return
            if node.left:
                depthFirstSearch(node.left, depth+1)
            results[depth] = node.val
            if node.right:
                depthFirstSearch(node.right, depth+1)

        results = {}
        depthFirstSearch(root, 0)

        # FORMAT OUTPUT
        counter = 0
        resultsArr = []
        while (counter in results):
            resultsArr.append(results[counter])
            counter+=1

        return resultsArr


myRoot = TreeNode(1)
myRoot.left = TreeNode(2)
myRoot.left.right = TreeNode(5)
myRoot.right = TreeNode(3)
myRoot.right.right = TreeNode(4)

sol = Solution()
print(sol.rightSideView(myRoot))

