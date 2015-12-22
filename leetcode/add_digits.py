# https://leetcode.com/problems/add-digits/
#  Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# 
# For example:
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime? 


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
