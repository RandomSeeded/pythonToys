# https://leetcode.com/problems/find-median-from-data-stream/

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# Examples:
# 
# [2,3,4] , the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
#     void addNum(int num) - Add a integer number from the data stream to the data structure.
#     double findMedian() - Return the median of all elements so far.
# 
# For example:
# 
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3) 
# findMedian() -> 2

# So, thing that jumps out at me is that we probably want a sorted data structure, due to our needing to be able to find the middle two values at any point in time. We can't just keep track of those two, because they may change over time. Add a bunch of larger values? What are the new mids? No frickin idea! Etc. So in order to do this properly, each value we add needs to at minimum know the one value next smaller, and the one value next larger, aka be sorted. 
# So what data structures could be good for that? Lists will be slow insertion and lookup (though we could improve lookup by keeping track of the two midpoints). 
# Sorted tree, probably.

# let's try out a 2-3 b tree
# Good idea, but this is going to run into serious issues when there's repeats. What can we do about that? Ewwwwwwww. Let's for now imagine there were no dups? That's not the best way to do this. Crap.


# BETTER SOLUTION: do it with priority queues (max-heap & min-heap?)
# 

import heapq
class MedianFinder:
    def __init__(self):
        self.smaller = []
        self.larger = []
        """
        Initialize your data structure here.
        """

    def __repr__(self):
        return "smaller: "+str(self.smaller) + " | larger: "+str(self.larger)
        

    def addNum(self, num):
        # If two queues are of same length, add to larger (may need to swap w/ one in smaller)
        if len(self.smaller) == len(self.larger):
            if len(self.larger) == 0:
                heapq.heappush(self.larger, num)
            else:
                largestSmall = -1 * heapq.heappop(self.smaller)
                heapq.heappush(self.larger, max(largestSmall, num))
                heapq.heappush(self.smaller, min(largestSmall, num) * -1)
            return

        # Otherwise, the larger always contains the extra. 
        else:
            midpoint = heapq.heappop(self.larger)

        # Push the prev midpoint and the new number onto the heaps
        if num < midpoint:
            heapq.heappush(self.smaller, -1 * num)
            heapq.heappush(self.larger, midpoint)
        else: 
            heapq.heappush(self.larger, num)
            heapq.heappush(self.smaller, -1 * midpoint)

        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        

    def findMedian(self):
        if len(self.larger) > len(self.smaller):
            median = heapq.heappop(self.larger)
            heapq.heappush(self.larger, median)
        else:
            mid1 = -1 * heapq.heappop(self.smaller)
            mid2 = heapq.heappop(self.larger)
            median = (float(mid1) + float(mid2)) / 2
            heapq.heappush(self.smaller, -1 * mid1)
            heapq.heappush(self.larger, mid2)
        return median
        """
        Returns the median of current data stream
        :rtype: float
        """

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(-1)
print(mf)
print(mf.findMedian())
mf.addNum(-2)
print(mf)
print(mf.findMedian())
mf.addNum(-3)
print(mf)
print(mf.findMedian())

