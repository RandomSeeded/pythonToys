# https://leetcode.com/problems/permutation-sequence/
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
# 
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.

# Idea: EASIEST WAY to do this would be to generate all the permutations, and then pick the kth. We could also short-cut this.
# HOWEVER, we could maybe just math this...how?

# THE SLOW SOLUTION THAT WAS GOOD PRACTICE
class slowSolution:
    def getPermutation(self, n, k):
        seen = {}
        def getAllPermutations(nums):
            if len(nums) == 1:
                return [[nums[0]]]

            strNums = "".join([str(num) for num in nums])
            if strNums in seen:
                return seen[strNums]

            allPermutations = []
            for i in range(len(nums)):
                numCopy = nums[:]
                digit = numCopy.pop(i)
                subPermutations = getAllPermutations(numCopy)
                for perm in subPermutations:
                    allPermutations.append([digit] + perm)

            seen[strNums] = allPermutations
            return allPermutations

        return getAllPermutations(list(range(1,n+1)))[k-1]

# MATHY THOUGHTS

# 1/nth of total permutations will have the 1st element be 1
# Example: 1,2,3 (6 total permutations). 2 start with 1, 2 start with 2, 2 start with 3
# First digit: 1,1,2,2,3,3
# Total permutations: 6
# Total permutations / n: 2
# We then do Math.floor(k / (perms / n)) + 1
# # of permutations = n ! (given). D'oh, it's a damn clue
# OK, so we know what digit will be in first position
# Now we rinse and repeat, with REMAINDER from our division (check this)
# and the remaining #s, to get our second digit

# 1 2 3, get 4th permutation
# 4 / (6 / 3)
# 4 / 2
# first digit is in 2nd position (2)
# 2 x x
# CORRECT ANSWER: 2 3 1
# So we would need to pass to our sub-fn: [1,3], 2
# Where do we get the 2?
# It can be thought of in a sense as the 'remainder.' If we use our 9 example
# we have a total of 362,880 permutations
# With the 1st digit removed, we have a total of 40,320 permutations. 
# IF WE WANT THE 54,494th permutation...what do we want to pass to our second iteration through?
# We want the REMAINDER of 54494 / 40,320: 14174
# This can be thought of as our new k, for array [1,3,4,5,6,7,8,9]
# 14174 / (40320 / 8) = 2 (aka third position, which is 4)


# NOTE: original coded so that we were 0-bounding our k (first is 0th, etc)
# However, leetcode is 1-bounding
import math
class Solution:
    def getPermutation(self, n, k):
        k-=1
        def subPermutation(nums, k):
            n = len(nums)
            if n == 1:
                return [nums[0]]
            totalPermutations = math.factorial(n)
            firstPosition = int(math.floor(k / (totalPermutations / n)))
            firstDigit = nums.pop(firstPosition)
            remainder = k % math.factorial(n-1)
            return [firstDigit] + subPermutation(nums, remainder)

        return "".join(str(x) for x in subPermutation(list(range(1, n+1)), k))

    # totalPermutations = math.factorial(n)
    # firstDigit = math.floor(k / (totalPermutations / n)) + 1

    # return firstDigit


sol = Solution()
# print(sol.getAllPermutations([1,2,3,4,5,6,7,8,9]))
# print(sol.getPermutation(6,5))
# print(sol.getPermutation(1,1))
# print(sol.getPermutation(9, 54494))
# print(sol.getPermutation(2, 2))
print(sol.getPermutation(9, 40320))



