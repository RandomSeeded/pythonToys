# https://leetcode.com/problems/majority-element-ii/

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

# LINEAR TIME: easy. 
# CONSTANT SPACE: less easy.
# note: there will be a maximum of two elements that appear more than n/3 times. Not sure if this helps us or not


# POSSIBILITIES:
# 1) Two elements appear more than n/3 times
# 2) One element appears more than n/3 times
# 3) No elements appear more than n/3 times

class Solution:
    def majorityElement(self, nums):
        top_num = None
        top_counter = 0
        second_num = None
        second_counter = 0

        # STOP: you need to think about the math of how this works out! When exactly do we want to re-assign? How do we want to increment?
        for num in nums:
            # Increment (positive) counters
            if num == top_num:
                top_counter += 1
            elif num == second_num:
                second_counter += 1
            # Re-assign numbers if a number has dropped off (paired away)
            elif top_counter == 0:
                top_num = num
                top_counter = 1
            elif second_counter == 0:
                second_num = num
                second_counter = 1
            # Lower counters
            else:
                top_counter -= 1
                second_counter -= 1

        results = [n for n in (top_num, second_num) if nums.count(n) > len(nums) / 3]
        return results

        # print('top_num', top_num)
        # print('top_counter', top_counter)
        # print('second_num', second_num)
        # print('second_counter', second_counter)

sol = Solution()
# sol.majorityElement([1,1,1,4,5])
# sol.majorityElement([1,1,1,4,4])
# print(sol.majorityElement([1,1,1,1,2,2,2,2,4,4,4]))
# print(sol.majorityElement([4,4,1,1,1,1,2,2,2,2,4]))
# print(sol.majorityElement([2,2]))
# print(sol.majorityElement([1,2]))
print(sol.majorityElement([0,0,0]))



























