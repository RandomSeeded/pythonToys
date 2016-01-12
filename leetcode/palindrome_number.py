# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        stringified = str(x)
        for i in range(len(stringified)):
            if stringified[i] != stringified[len(stringified)-1-i]:
                return False

        return True
        """
        :type x: int
        :rtype: bool
        """
        
sol = Solution()
print(sol.isPalindrome(1234))
print(sol.isPalindrome(1221))
print(sol.isPalindrome(121))


