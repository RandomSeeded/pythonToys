# https://leetcode.com/problems/minimum-path-sum/
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.

# GO DOWN & RIGHT
# GET TO END
# PICK MIN.
# (recursive)

# NOTE: we aren't supposed to just return the sum, actually the path? Nah, rtype int


#OKAY : this solution works....but is time limit exceeded! Let's dynamic programming this
class slowSolution:
    def minPathSum(self, grid, row=0, col=0, sum=0):
        height = len(grid)
        width = len(grid[0])
        if row == height-1 and col == width -1:
            return sum+grid[row][col]

        downSum = self.minPathSum(grid, row+1, col, sum) if row < height-1 else float('inf')
        rightSum = self.minPathSum(grid, row, col+1, sum) if col < width-1 else float('inf')

        return grid[row][col] + min(downSum, rightSum)

class Solution:
    def minPathSum(self, grid, row=0, col=0, sum=0, storage={}):
        if str(row)+","+str(col) in storage:
            return storage[str(row)+","+str(col)]
        height = len(grid)
        width = len(grid[0])
        if row == height-1 and col == width -1:
            return sum+grid[row][col]

        downSum = self.minPathSum(grid, row+1, col, sum, storage) if row < height-1 else float('inf')
        rightSum = self.minPathSum(grid, row, col+1, sum, storage) if col < width-1 else float('inf')

        result = grid[row][col] + min(downSum, rightSum)
        storage[str(row)+","+str(col)] = result
        print('result', result)
        return result;


myGrid = [[0,0],[0,0]]
# myGrid = [[1,2,3],[4,5,6],[7,8,9]]
# myGrid = [[1,2,5],[3,2,1]]

sol = Solution()
print(sol.minPathSum(myGrid))


