# https://leetcode.com/problems/range-sum-query-immutable/

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# Note:
# 
#     You may assume that the array does not change.
#     There are many calls to sumRange function.

# Intelligent solution: an accumulator array
class NumArray:
    def __init__(self, nums):
        total = 0
        self.accumulator = []
        for i in range(len(nums)):
            total += nums[i];
            self.accumulator.append(total)

    def sumRange(self, i, j):
        return self.accumulator[j] - self.accumulator[i-1] if i > 0 else self.accumulator[j]


# The recursive solution exceeded maximum depth. We can still store results for every possibility, but perform with a for loop. Let's do that
class recursiveDynamic(object):
    def __init__(self, nums):
        self.nums = nums
        self.memo = {}

    def sumRange(self, i, j):
        result = 0
        for idx in range(i, j+1):
            remainingKey = str(idx) + ":" + str(j)
            if remainingKey in self.memo:
                return result + self.memo[remainingKey]
            else:
                currKey = str(i) + ":" + str(idx)
                result += self.nums[idx]
                self.memo[currKey] = result

        key = str(i) + ":" + str(j)
        self.memo[key] = result
        return result


# Less simple solution: a recursive call and dynamic programming (because there are MANY calls to sumRange)
class recursiveNumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.memo = {}

    def sumRange(self, i, j):
        key = str(i)+":"+str(j)
        if key in self.memo:
            return self.memo[key]
        elif i == j:
            self.memo[key] = self.nums[i]
            return self.nums[i]
        else:
            result = self.nums[i] + self.sumRange(i+1, j)
            self.memo[key] = result
            return result



# Simple solution - a for loop over the array:
class simmpleNumArray(object):
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i, j):
        result = 0
        for idx in range(i, j+1):
            result += self.nums[idx]
        return result
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 1))
print(numArray.sumRange(1, 2))

