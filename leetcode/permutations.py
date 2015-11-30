# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]

        results = []
        for i in range(len(nums)):
            numsCopy = nums[:]
            firstNum = numsCopy[i]
            del numsCopy[i]
            subPermutations = self.permute(numsCopy)
            print('subpermutations', subPermutations)
            for permutation in subPermutations:
                results.append([firstNum] + permutation)

        return results

