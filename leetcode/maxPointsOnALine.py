# https://leetcode.com/problems/max-points-on-a-line/

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Idea: generate all possible lines between all possible points. See if any other points exist on the same line.
# Problem: the complexity of this is shit. Because it's n^3 (n^2 to generate all lines, and then to check against each)
# Oh well

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):

        # Store maximum points on a line
        maxPointsOnLine = 0

        # Loop over all possible lines
        for a in range(0, len(points)-2):
            for b in range(a+1, len(points)-1):

                # Calculate the slope and intercept for the line between these two points
                pointA = points[a]
                pointB = points[b]
                if (pointB.x == pointA.x):
                    slope = "Vertical"
                else:
                    slope = (pointB.y - pointA.y) / (pointB.x - pointA.x)
                    intercept = pointB.y - slope*pointB.x

                # Find any other points that are on this line
                curPointsOnLine = 0
                for c in range(0, len(points)-1):
                    pointC = points[c]
                    
                    if slope == "Vertical":
                        curPointsOnLine += 1 if pointC.x == pointB.x else 0
                    else:
                        projectedY = slope*pointC.x + intercept
                        if (projectedY == pointC.y):
                            curPointsOnLine += 1

                if curPointsOnLine > maxPointsOnLine:
                    maxPointsOnLine = curPointsOnLine

        return maxPointsOnLine

            
