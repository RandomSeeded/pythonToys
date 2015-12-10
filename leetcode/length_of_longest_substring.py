# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

# THOUGHTS: can we do this linearly?
# What if we have a string of all the currently unique characters? When we see a repeat, what would we do? We would want to remove all characters in our currently unique string that occured BEFORE (including) the first character we saw twice.

# One way we could do that: have two data structures, one a hash (for fast lookup) and one an array/stack with our characters in it.

# We would then just loop over the stack to remove the chars (and also remove from the hash in const time apiece)

import collections
class Solution:
    def lengthOfLongestSubstring(self, s):
        seenQueue = collections.deque()
        seenHash = {}
        maxLength = 0
        currentLength = 0
        for letter in s:
            if letter in seenHash:
                queueLetter = seenQueue.popleft()
                del seenHash[queueLetter]
                while (queueLetter != letter):
                    queueLetter = seenQueue.popleft()
                    del seenHash[queueLetter]
                currentLength = len(seenQueue)

            seenHash[letter] = True
            seenQueue.append(letter)
            currentLength += 1
            if currentLength > maxLength:
                maxLength = currentLength

        return maxLength

sol = Solution()
# print(sol.lengthOfLongestSubstring('abcabcbb'))
# print(sol.lengthOfLongestSubstring('bbbbbbb'))
# print(sol.lengthOfLongestSubstring('aab'))


