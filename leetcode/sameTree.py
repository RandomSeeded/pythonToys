# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif (p == None or q == None) and (p != None or q != None):
            return False
        elif (p.val != q.val):
            return False
        else:
            left_same = self.isSameTree(p.left, q.left)
            right_same = self.isSameTree(p.right, q.right)
            return left_same and right_same
