# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# 
# The flattened tree should look like:
# 
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

# Not in-place seems easy enough: we simply do a depth-first search on the tree, add to results linked list, return that list.
# What does it mean to flatten a tree 'in-place'?
# It means we turn the tree nodes into linked list nodes. Instead of having a left and a right, it instead has a next.
# What will the value of next be?
# If it has a left, it's clearly the left. If it has no left but a right, then it's the right. The difficulty is what if it has neither left nor right? 
# We just pass a ref to the 'next' thing for the first time when that occurs
# Constant space. Bam. Wham bam whatcha.
# Definition for a binary tree node.
# Ew no we can't just pass a single ref to next, it does need to be a queue of some sort. E.g. the 'next' on 3 is 4, but the next on 4 is 5.

from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        nexts = deque()
        def inner(node):
            if not node:
                return
            if node.left:
                node.next = node.left
                if node.right:
                    nexts.appendleft(node.right)
                inner(node.left)
            elif node.right:
                node.next = node.right
                inner(node.right)
            else:
                if len(nexts) > 0:
                    node.next = nexts.popleft()

        inner(root)




root = TreeNode(5)
sol = Solution()
sol.flatten(root)

