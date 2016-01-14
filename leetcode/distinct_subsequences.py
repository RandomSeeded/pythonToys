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

# So what's different about counting?
# CASE #1: no repeated characters in T (e.g. ABCDE)
# If S has repeated characters, we can math it, e.g. AABCDE (2)
# What if there are repeated sequences? E.g. ABABCDE? 3 solutions (01, 03, 23)
# Is that solvable linearly? Not that I can see. LETS GO TO BRUTE FORCE METHOD see what happens
# Mild issue: how do you tell what index you're removing from the original string? Mild pain in the ass. Answer: we just pass in the original string and re-modify each time

class Solution(object):
    def __init__(self):
        self.seen = {}

    def numDistinct(self, s, t, removed = {}):
        # Re-generate the substring
        substring = ""
        for i in range(len(s)):
            if i not in removed:
                substring += s[i]
        print('generating for substring', substring)

        result = 0
        if substring == t:
            result = 1
        elif len(substring) <= len(t):
            result = 0
        else:
            # Return saved value from hash
            if substring in self.seen:
                print('Seen this substr before', substring, self.seen[substring])
                return self.seen[substring]

            for i in range(len(s)):
                if i not in removed:
                    # Idea here: we will remove all new indices one at a time, and recurse. We will add the newly removed index to removed and pass it along as a parameter. 
                    # ONE ISSUE: we will probs need to remove the indices from removed when we pass back up. Not a big deal
                    removed[i] = True
                    newSubstring = ""
                    for j in range(len(s)):
                        if j not in removed:
                            newSubstring += s[j]
                    result += self.numDistinct(s, t, removed)
                    del removed[i]

        # Save value in hash and return result
        self.seen[substring] = result
        print('result for substring', substring, result)
        return result

        
sol = Solution()
print(sol.numDistinct('rabbbiit', 'rabbit'))
# THE ABOVE IS INCORRECTLY RETURNING 12, but should be 6. Why? Because we're counting the same paths twice.
# print(sol.numDistinct("anacondastreetracecar", "contra"))


