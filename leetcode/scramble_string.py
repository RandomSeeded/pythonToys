# https://leetcode.com/problems/scramble-string/
#  Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
# 
# Below is one possible representation of s1 = "great":
# 
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# 
# To scramble the string, we may choose any non-leaf node and swap its two children.
# 
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
# 
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# 
# We say that "rgeat" is a scrambled string of "great".
# 
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
# 
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# 
# We say that "rgtae" is a scrambled string of "great".
# 
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1. 


# WAYS WE COULD DO THIS
# Non-binary string: check to see if the character counts for the two are equivalent (order n)
# class Solution:
#     def isScramble(self, s1, s2):
#         s1Count = {}
#         s2Count = {}
#         for letter in s1:
#             s1Count[letter] = s1Count[letter]+1 if letter in s1Count else 1
#         for letter in s2:
#             s2Count[letter] = s2Count[letter]+1 if letter in s2Count else 1
# 
#         for letter in s1Count:
#             if letter not in s2Count or s1Count[letter] != s2Count[letter]:
#                 return False
# 
#         for letter in s2Count:
#             if letter not in s1Count or s1Count[letter] != s2Count[letter]:
#                 return False
# 
#         return True
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """

# The above is functional for my understanding of the problem, but outputs that 'bdac' is a scrambled string of 'abcd'. Why is it not?

# Because we're asking only very specifically for binary trees, apparently. So the reason is because: if we have abcd in a binary tree:

# abcd
# / \
# ab   cd
# a  b   c   d

# There's no way that we're going to have, for example, a c in between a and b

