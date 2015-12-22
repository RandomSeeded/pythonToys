# https://leetcode.com/problems/add-digits/
#  Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# 
# For example:
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime? 

# HARD VERSION: constant runtime, not even a loop?
class Solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        remainder = num % 9
        return remainder if remainder != 0 else 9

# EASY VERSION (recursion)
class Solution:
    def addDigits(self, num):
        stringified = str(num)
        if len(stringified) == 1:
            return num
        else:
            total = 0
            for i in range(len(stringified)):
                total += int(stringified[i])
            return self.addDigits(total)

sol = Solution()
print(sol.addDigits(38))

# POSSIBLE RESULTS: not 0-9, actually they're 1-9
# Can we easily check? Aka just loop through 1-9 and check each of these?
# Well, sort of 0-9. Anyway, can we check constant time on that?

# How can we check if a solution is correct besides adding em up?
# OK, googling shows it's related to 9s. 38 % 9 = 2. Huh
# 692 % 9 = 8
# 692 : 17: 8
# who knew? I did not.

