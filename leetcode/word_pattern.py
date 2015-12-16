# https://leetcode.com/problems/word-pattern/

# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# 
# Examples:
# 
#     pattern = "abba", str = "dog cat cat dog" should return true.
#     pattern = "abba", str = "dog cat cat fish" should return false.
#     pattern = "aaaa", str = "dog cat cat dog" should return false.
#     pattern = "abba", str = "dog dog dog dog" should return false.
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space. 

class Solution:
    def wordPattern(self, pattern, str):
        seen = {}
        seenWords = {}
        letters = list(pattern)
        words = str.split()

        if len(words) != len(letters):
            return False

        for (letter, word) in zip(letters, words):
            if word in seenWords:
                if seenWords[word] != letter:
                    return False
            if letter in seen:
                if seen[letter] != word:
                    return False
            else:
                seen[letter] = word
                seenWords[word] = letter

        return True





sol = Solution()
print(sol.wordPattern('abba', 'dog cat cat dog'))
print(sol.wordPattern('abba', 'dog cat cat fish'))
print(sol.wordPattern('abba', 'dog dog dog dog'))





