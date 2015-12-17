# https://leetcode.com/problems/move-zeroes/

#  Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# 
# Note:
# 
#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.

# Issue here is obviously the in-place. Otherwise, you'd just make a new array, push all non-zeros in, then push all the zeros in at the end
# We can still take that general approach. Use a loop to loop over the array. Use a counter to mark the number of zeros. Math out which position we need to put each element into. Let's do it:

# 0 1 0 3 12
# 1 1 0 3 12
# 1 3 0 3 12
# 1 3 12 3 12
# 1 3 12 0 0

class Solution:
    def moveZeros(self, nums):
        nonZeroCounter = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[nonZeroCounter] = nums[idx]
                nonZeroCounter+=1

        while nonZeroCounter < len(nums):
            nums[nonZeroCounter] = 0
            nonZeroCounter += 1

        # (note that leetcode version doesn't expect a return value)
        return nums

sol = Solution()
print(sol.moveZeros([0,1,0,3,12]))




