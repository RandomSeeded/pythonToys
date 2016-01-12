# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        # Ensure lengths are the same
        if len(s) != len(t):
            return False

        seen1 = {}
        seen2 = {}

        for c1, c2 in zip(s, t):
            if c1 in seen1:
                if seen1[c1] != c2:
                    return False
            else:
                seen1[c1] = c2

            if c2 in seen2:
                if seen2[c2] != c1:
                    return False
            else:
                seen2[c2] = c1

        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

sol = Solution()
print(sol.isIsomorphic('egg','add'))
print(sol.isIsomorphic('foo','bar'))
print(sol.isIsomorphic('paper','title'))
