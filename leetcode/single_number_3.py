# https://leetcode.com/problems/single-number-iii/
#  Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
# 
# For example:
# 
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
# 
# Note:
# 
#     The order of the result is not important. So in the above example, [5, 3] is also correct.
#     Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

# WITH LINEAR SPACE COMPLEXITY: easy, use a hash. 
class bigSolution:
    def singleNumber(self, nums):
        seenOnce = {}
        for num in nums:
            if num in seenOnce:
                del seenOnce[num]
            else:
                seenOnce[num] = True

        results = []
        for num in seenOnce:
            results.append(num)

        return results

# BUT WHAT ABOUT WITH CONSTANT SPACE (and still linear time?)
# Apparently this can be done bitwise. Figure it out

sol = Solution()
print(sol.singleNumber([1,2,1,3,2,5]))



