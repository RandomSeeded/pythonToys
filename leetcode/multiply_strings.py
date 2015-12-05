# https://leetcode.com/problems/multiply-strings/
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note: The numbers can be arbitrarily large and are non-negative.

# What makes this difficult? Maybe the fact that they can be arbitrarily large?

# The naive way:
class Solution:
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))


# Nope...turns out it is indeed that easy. This was a stupid problem.

sol = Solution()
print(sol.multiply('3','4'))
