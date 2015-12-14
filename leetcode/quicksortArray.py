# One question about array implementation: how do we best make sure we are 

# Non-constant space
class Solution:
    def quicksortArray(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[0]
        lessThanPivot = []
        greaterThanPivot = []
        for i in range(1, len(nums)):
            if nums[i] < pivot:
                lessThanPivot.append(nums[i])
            else:
                greaterThanPivot.append(nums[i])

        return self.quicksortArray(lessThanPivot) + [pivot] + self.quicksortArray(greaterThanPivot)

# Constant space (in-place swaps)
class constantSolution:
    def quicksortArray(self, nums, start=0, end=None):
        if not end:
            end = len(nums)

sol = Solution()
print(sol.quicksortArray([1,2,3,4,5]))
print(sol.quicksortArray([5,4,3,2,1]))
print(sol.quicksortArray([1,3,2,4,5]))
print(sol.quicksortArray([4,3,1,2,5]))


