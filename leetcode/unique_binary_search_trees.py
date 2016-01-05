# https://leetcode.com/problems/unique-binary-search-trees/

# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# How many possibilities for the root? N
# If the root is 1, we have two options
# If the root is 3, we have two options
# However, if the root is 2, we only have ONE option. 
# What determines that? The 1 can only go in one place. The 3 can only go in one place.
# A different way of phrasing that: there exists exactly one element that can go to the left of the node and exactly one element that can go to the right of the node
# If we had 2 as root, and 1 3 4 remaining, we have exactly one element that can go the left of the node, and 2 that can go to the right. So we have two solutions. 
# N is 2: how many trees? 2
# N is 3: how many trees? 5
# N is 4: how many trees? 
# How could we break this down? We plug each into the root.
# If 1 is the root: we have 5 trees (from n == 3)
# If 2 is the root: lets examine the subtrees. To the left we have only one option. To the right we have two children, giving us two trees. So total trees for 2 is 2
# If 3 is the root: to the right we have one children, only one possible tree. To the left we have two children, giving us two possible trees
# If 4 is the root: to the right we have no children, to the left we have three, giving us 5 possible trees.
# TOTAL: 5 + 2 + 2 + 5 = 14
# What if we had a situation where we had two possible children to the left and two possible to the right? Then there would be four total possible trees. Possibilities will be multiplicative
# So, approach: we will handle this similar to a fibonacci case. 

class Solution:
    def __init__(self):
        self.memo = {0:1,1:1,2:2}
    def numTrees(self, n):
        if n in self.memo:
            return self.memo[n]
        else:
            result = 0
            for i in range(1, n+1):
                result += (self.numTrees(i-1) * self.numTrees(n-i))
            self.memo[n] = result
            return result

sol = Solution()
print(sol.numTrees(0))
print(sol.numTrees(1))
print(sol.numTrees(2))
print(sol.numTrees(3))
print(sol.numTrees(4))
