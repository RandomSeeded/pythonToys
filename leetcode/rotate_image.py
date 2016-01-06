# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Follow up:
# Could you do this in-place?

# THOUGHTS: neither seems that bad. 
# Let's start with not-in-place
class Solution(object):
    def rotate(self, matrix):
        matrix[1][1] = 7
        def rotatePixel(i, j):
            # Split it out by quadrants, do the math
            return 1,1

        # Init matrix
        newMatrix = [0] * len(matrix)
        for i in range(len(matrix)):
            newMatrix[i] = [0] * len(matrix)

        # Rotate
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                x, y = rotatePixel(i, j)
                newMatrix[i][j] = matrix[x][y]

        # Copy over
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = newMatrix[i][j]

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        

sol = Solution()
matrix = [[1,2],[3,4]]
sol.rotate(matrix)
print(matrix)
