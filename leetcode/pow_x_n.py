# https://leetcode.com/problems/powx-n/
# Implement pow(x, n). 
# NOTE: not finished

class Solution(object):
    def myPow(self, x, n):
        total = x;
        for i in range(1, n):
            total *= x
        return total

mySol = Solution()
print mySol.myPow(2,3);

