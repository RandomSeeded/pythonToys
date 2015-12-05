# https://leetcode.com/problems/repeated-dna-sequences/
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
# 
# For example,
# 
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# 
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
class Solution:
    def findRepeatedDnaSequences(self, s):
        seen = {}
        results = []
        for i in range(len(s) - 9):
            substr = s[i:i+10]
            if substr not in seen:
                seen[substr] = 1
            else:
                seen[substr] += 1
                if seen[substr] == 2:
                    results.append(substr)

        return results


sol = Solution()

