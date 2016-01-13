# https://leetcode.com/problems/distinct-subsequences/

# Given a string S and a string T, count the number of distinct subsequences of T in S.
# 
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# 
# Here is an example:
# S = "rabbbit", T = "rabbit"
# 
# Return 3. 

# OK, so here's how it works. You can REMOVE characters from S. You cannot remove characters from T. After removing characters from S, S needs to exactly equal T?

# EASIEST WAY TO DO IT
# Brute force: delete chars, recurse. 
# Optimizations: cut out of length too small (s < t), dynamic programming (hash)

# IS THERE A BETTER WAY?
# How could we do it in a boolean fashion? i.e. is there one or not?
# We would loop through s and t. If s equalled the next t, advance, etc.
# Things get trickier though once we have to deal with repeat letters. Other than that, the shit's EZ...but we can probably just solve that with math.
# Let's start with the boolean case

class boolSolution(object):
    def numDistinct(self, s, t):
        tIndex = 0
        for i in range(len(s)):
            if s[i] == t[tIndex]:
                tIndex+=1

        if tIndex == len(t):
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: int
        """
class Solution(object):
    def numDistinct(self, s, t):
        pass

        
sol = Solution()
print(sol.numDistinct('rabbbit', 'rabbit'))


