# https://leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# So in linear time and linear space, this is super easy:

# CONSTANT SPACE SOLUTION
class Solution:
    def majorityElement(self, nums):
        majority_num = 0
        counter = 0
        for num in nums:
            if counter == 0:
                majority_num = num
            if majority_num != num:
                counter -= 1
            else:
                counter += 1

        return majority_num

# EASY, NON-CONSTANT-SPACE SOLUTION
class largeSolution:
    def majorityElement(self, nums):
        counters = {}
        for num in nums:
            counters[num] = counters[num] + 1 if num in counters else 1
            if counters[num] > len(nums) / 2:
                return num


sol = Solution()
print(sol.majorityElement([1,2,3,1,1]))





