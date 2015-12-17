# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: you're going to need to check every single node, so it really doesn't matter whether we DFS or BFS. Might as well DFS because it's easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root, depth = 1):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return depth
        else:
            return max(self.maxDepth(root.left, depth+1), self.maxDepth(root.right, depth+1))
        """
        :type root: TreeNode
        :rtype: int
        """
        
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(6)
sol = Solution()
print(sol.maxDepth(root))
