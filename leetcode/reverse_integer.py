# https://leetcode.com/problems/reverse-integer/
# Reverse digits of an integer.
# 
# Example1: x = 123, return 321
# Example2: x = -123, return -321 

class Solution:
    def reverse(self, x):
        # handle negatives
        if x < 0:
            sign = -1
            x = x * -1
        else:
            sign = 1

        result = ""
        stringified = str(x)
        for c in stringified:
            result = c + result

        return sign * int(result)

sol = Solution()
print(sol.reverse(-123))
