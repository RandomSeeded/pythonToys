# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# We can do this recursively. How?
# For each house, we rob or don't rob based on the maximum of algoing either the remaining houses at idx + 1 or idx + 2

class Solution(object):
    def rob(self, nums):
        maxes = {}
        totalMax = 0
        for i in range(0, len(nums)):
            maxA = maxes[i-2] if i-2 in maxes else 0
            maxB = maxes[i-3] if i-3 in maxes else 0
            maxes[i] = nums[i] + max(maxA, maxB)
            if (maxes[i] > totalMax):
                totalMax = maxes[i]
        return totalMax

sol = Solution()
# print(sol.rob([1,1,1]))
# print(sol.rob([1,2,1.5]))
# print(sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,21]))

print(sol.rob([155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]))


