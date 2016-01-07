# https://leetcode.com/problems/shortest-palindrome/
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
# 
# For example:
# 
# Given "aacecaaa", return "aaacecaaa".
# 
# Given "abcd", return "dcbabcd".

# THOUGHTS: OK, you can always make a palindrome this way by adding 2nd-thru-end chars to start.
# (see the abcd -> dcbabcd example)
# However, in some situtations we can come up with a shorter method.
# Really, another way of expressing that would be: GIVEN abcdcba, does there exist in there something we could cut off to make a shorter pal?
# aacecaaa: becomes aaacecaaacecaaa
# We then start in the middle (aacecaaa) and work outwards towards the left and return the first palindrome we find.
# that should work, though there may be more efficient ways of doing this
