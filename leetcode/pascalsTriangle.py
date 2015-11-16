# 
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# 
# 

class Solution(object):
    def generate(self, numRows):
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            prev = self.generate(numRows-1)
            last = prev[len(prev)-1]
            new = []
            for i in range(0, len(last)+1):
                a = last[i-1] if i-1 >= 0 else 0
                b = last[i] if i < len(last) else 0
                new.append(a+b)
            prev.append(new)
            return prev

        """
        :type numRows: int
        :rtype: List[List[int]]
        """

sol = Solution()
# print(sol.generate(1))
# print(sol.generate(2))
# print(sol.generate(3))
# print(sol.generate(4))
# print(sol.generate(5))
print(sol.generate(6))


