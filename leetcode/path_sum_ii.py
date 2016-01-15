# https://leetcode.com/problems/path-sum-ii/


# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
# 
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 
# return
# 
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# GENERAL APPROACH: depth first search this again. However, this time just add to results instead of returning T/F

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        results = []

        def searchTree(node, currSum, path):
            # Base case 1: this is not a node
            if node == None:
                return

            # Base case 2: this node is a leaf
            if node.left == None and node.right == None:
                if currSum + node.val == sum:
                    print('bam')
                    path.append(node.val)
                    results.append(path)

            # Otherwise recurse til we are at a leaf
            else:
                currSum += node.val
                path.append(node.val)
                searchTree(node.left, currSum, path[:]) 
                searchTree(node.right, currSum, path[:])

        searchTree(root, 0, [])
        return results
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
       
