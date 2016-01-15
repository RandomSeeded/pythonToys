# https://leetcode.com/problems/path-sum/
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
# 
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# We can just depth-first-search this. Let's do that

class Solution(object):
    def hasPathSum(self, root, sum):
        def searchTree(node, currSum):
            # Base case 1: this is not a node
            if node == None:
                return False

            # Base case 2: this node is a leaf
            if node.left == None and node.right == None:
                return currSum + node.val == sum

            # Otherwise recurse til we are at a leaf
            else:
                currSum += node.val
                return searchTree(node.left, currSum) or searchTree(node.right, currSum)

        return searchTree(root, 0)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

root = TreeNode(5)
root.left = TreeNode(8)
sol = Solution()
print(sol.hasPathSum(root, 13))
print(sol.hasPathSum(root, 12))
       
