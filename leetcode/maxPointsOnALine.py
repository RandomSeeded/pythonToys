# https://leetcode.com/problems/max-points-on-a-line/

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Idea: generate all possible lines between all possible points. See if any other points exist on the same line.
# Problem: the complexity of this is shit. Because it's n^3 (n^2 to generate all lines, and then to check against each)
# Oh well

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1

        maxPointsOnLine = 0

        for a in range(0, len(points)):
            D = {}
            for b in range(0, len(points)):
                pointA = points[a]
                pointB = points[b]
                if pointB.x == pointA.x and pointA.y == pointB.y:
                    slope = "Same Point"
                elif (pointB.x == pointA.x):
                    slope = "Vertical"
                else:
                    slope = (pointB.y - pointA.y) / (pointB.x - pointA.x)

                if (slope in D):
                    D[slope] += 1;
                else:
                    D[slope] = 1;

                if D[slope] > maxPointsOnLine:
                    maxPointsOnLine = D[slope]

        return maxPointsOnLine
