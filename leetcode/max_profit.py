# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# THOUGHTS: we want to go from the lowest low to the highest high
# So from left to right, we want to go from the local minima to the local maxima
# So we can keep track of a few things:
# 1) how much money we've made
# 2) current local minimum
# 3) current local maximum

# We need to be aware of if we're moving down or up
# If we're moving down, then we want to lock in previous profit
# If we're moving up, keep going

# note: this is going to be insufficient.
# why: what if we have a global minimum and then a local max, but later there's a BIGGER max?
# we could handle in one trade. Or could we?

# 2, [1,2,4,2,5,7,2,4,9,0]
# CORRECT ANSWER (max 2 trades): 1->7 (6), 2->9 (7). Total of 13
# However, my answer will currently go 1-4 (3), 2->7 (5), 2->9 (6): Total of 12 (1-4 chopped)
# Fundamental problem is handling global vs local. Not sure we can do this linearly anymore.

# SO: new thought. Ignore complexity atm
# Imagine we have everything marked as local mins/maxes. We can totally do that
# What would we do with that/how do we handle? Optimize further later
# We don't want to add a local min/max pair if there exists a local min/max pair of greater range which includes it in that range

# Imagine we had 1, 3, 2, 4
# If we had stored, 0/1, 2/3 how could we test this? note: not straddled, so can't be based on index necessarily
# If we instead stored 1/3, 2/4 could we check on that? We also need to be aware of index. Do we? Why? Not if they're stored in order...
# What exactly is causing this here? Two ways to look at it:
# 1) 2 is incorrectly assigned to be a minima
# 2) 3 is incorrectly assigned as a maximum
# (Really, both are true)

# OK, what if we approach this COMPLETELY DIFFERENTLY:
# note  that this would be significantly slower
# if we wanted ONLY 1, how could we do this?
# We loop through, storing the max profit we've seen and the lowest we've seen
# We compare each to the lowest we've seen

# NOW BACK TO FASTER SOLUTIONS:
# we can use our original attempt at a fast solution to create a list of pairs. So far so fast (linear)
# All we then need to do is loop over that again (still linear) to resolve any cases where that's insuff.
# You say that like it's easy. How can we do that?
# What makes a trade valid? If there exists NO LOWER MINIMUMS TO THE LEFT and NO HIGHER MAXIMUMS TO THE RIGHT
# No, not quite. Imagine 1, 4, 2, 3. 2/3 is still totally valid, even though there exists a lower min to the left. Fuck.
# However, 1,3,2,4 -> should get collapsed to 1-4

# Why does 1-4, 2-3 not get collapsed? Because even though 1-3 is better than 2-3, 1 is already taken by something better

# So we can describe things as outer and inner
# What DOES get collapsed?

# (higher mags relative to some 'middle')
# BOTH OUTER ARE HIGHER MAGNITUDE: collapse (e.g. 1-3, 2-4 --> 1-4)
# ONE OUTER IS HIGHER MAGNITUDE: do not collapse (e.g. 1-5, 2-4) [left of higher mag]
# NEITHER OUTER IS OF HIGHER MAGNITUDE: do not collapse (e.g. 2-8, 1-6)

# ISSUE: what if we have THREE or more trades?
# E.g. 1-5, 2-4 (not collapse), BUT ALSOOOOOOO 3-7
# Single best would be 1-7. This is brutal.

# THE BEST SOLUTION
class Solution(object):
    def maxProfit(self, k, prices):
        if len(prices) <= 1:
            return 0

        profitableTrades = []
        lastPrice = prices[0]
        localMin = lastPrice
        localMax = lastPrice
        for i in range(1, len(prices)):
            if prices[i] < lastPrice:
                profitableTrades.append([localMin, localMax])
                # profitableTrades.append(localMax - localMin)
                localMax = prices[i]
                localMin = prices[i]
            else:
                localMax = max(localMax, prices[i])
                localMin = min(localMin, prices[i])
                if i == len(prices)-1 and localMax - localMin > 0:
                    profitableTrades.append([localMin, localMax])

            lastPrice = prices[i]

        collapsedTrades = []
        loweridx = 0
        higheridx = 1
        while higheridx < len(profitableTrades):
            # Check if trades can be collapsed into one
            if profitableTrades[loweridx][0] <= profitableTrades[higheridx][0] and profitableTrades[loweridx][1] >= profitableTrades[higheridx][1]:
                # If they can, combine them, and iterate the higher index
                profitableTrades[loweridx] = [profitableTrades[loweridx][0],profitableTrades[higheridx][1]]
                higheridx+=1
            # If the trades cannot be combined into one, then what? 
            else:
            
        return profitableTrades

# What complexity can we get it down to if we start from both edges?
# We keep track of the smallest we see from the left, and the largest we see from the right
# So far this is going to yield no improvements over the other 1-at-a-time method

# THE INSUFFICIENT SOLUTION
# class Solution(object):
#     def maxProfit(self, k, prices):
#         if len(prices) <= 1:
#             return 0
# 
#         profitableTrades = []
#         lastPrice = prices[0]
#         localMin = lastPrice
#         localMax = lastPrice
#         for i in range(1, len(prices)):
#             if prices[i] < lastPrice:
#                 profitableTrades.append([localMin, localMax])
#                 # profitableTrades.append(localMax - localMin)
#                 localMax = prices[i]
#                 localMin = prices[i]
#             else:
#                 localMax = max(localMax, prices[i])
#                 localMin = min(localMin, prices[i])
#                 if i == len(prices)-1 and localMax - localMin > 0:
#                     profitableTrades.append([localMin, localMax])
# 
#             lastPrice = prices[i]
# 
#         return profitableTrades


        # now sum up
        # profitableTrades.sort()
        # print(profitableTrades[-k:])
        # return reduce(lambda x,y: x+y, profitableTrades[-k:])

sol = Solution()
print(sol.maxProfit(1, [1,3,2,4]))
# print(sol.maxProfit(10, [1,2,3,4,5,6,7,8,9,10]))
# print(sol.maxProfit(5, [10,9,8,7,6,5,4,3,2,1]))
# print(sol.maxProfit(5, [1,3,2,4,3,6,4,7]))
# print(sol.maxProfit(5, [1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10]))

# THE SLOW SOLUTION 
# class Solution(object):
#     def maxProfit(self, k, prices):
# 
#         maxProfit = 0
#         for iter in range(k):
#             largestGap = 0
#             lowestSeen = float('inf')
#             largestSeen = float('-inf')
#             minAt = 0
#             maxAt = 0
#             for idx in range(len(prices)):
#                 price = prices[idx]
#                 largestGap = max(largestGap, price-lowestSeen)
#                 if price > largestSeen:
#                     largestSeen = price
#                     maxAt = idx
#                 if price < lowestSeen:
#                     lowestSeen = price
#                     minAt = idx
#             maxProfit += largestGap
#             prices = prices[:minAt] + prices[maxAt+1:]
# 
#         return maxProfit

# print(sol.maxProfit(29, [70,4,83,56,94,72,78,43,2,86,65,100,94,56,41,66,3,33,10,3,45,94,15,12,78,60,58,0,58,15,21,7,11,41,12,96,83,77,47,62,27,19,40,63,30,4,77,52,17,57,21,66,63,29,51,40,37,6,44,42,92,16,64,33,31,51,36,0,29,95,92,35,66,91,19,21,100,95,40,61,15,83,31,55,59,84,21,99,45,64,90,25,40,6,41,5,25,52,59,61,51,37,92,90,20,20,96,66,79,28,83,60,91,30,52,55,1,99,8,68,14,84,59,5,34,93,25,10,93,21,35,66,88,20,97,25,63,80,20,86,33,53,43,86,53,55,61,77,9,2,56,78,43,19,68,69,49,1,6,5,82,46,24,33,85,24,56,51,45,100,94,26,15,33,35,59,25,65,32,26,93,73,0,40,92,56,76,18,2,45,64,66,64,39,77,1,55,90,10,27,85,40,95,78,39,40,62,30,12,57,84,95,86,57,41,52,77,17,9,15,33,17,68,63,59,40,5,63,30,86,57,5,55,47,0,92,95,100,25,79,84,93,83,93,18,20,32,63,65,56,68,7,31,100,88,93,11,43,20,13,54,34,29,90,50,24,13,44,89,57,65,95,58,32,67,38,2,41,4,63,56,88,39,57,10,1,97,98,25,45,96,35,22,0,37,74,98,14,37,77,54,40,17,9,28,83,13,92,3,8,60,52,64,8,87,77,96,70,61,3,96,83,56,5,99,81,94,3,38,91,55,83,15,30,39,54,79,55,86,85,32,27,20,74,91,99,100,46,69,77,34,97,0,50,51,21,12,3,84,84,48,69,94,28,64,36,70,34,70,11,89,58,6,90,86,4,97,63,10,37,48,68,30,29,53,4,91,7,56,63,22,93,69,93,1,85,11,20,41,36,66,67,57,76,85,37,80,99,63,23,71,11,73,41,48,54,61,49,91,97,60,38,99,8,17,2,5,56,3,69,90,62,75,76,55,71,83,34,2,36,56,40,15,62,39,78,7,37,58,22,64,59,80,16,2,34,83,43,40,39,38,35,89,72,56,77,78,14,45,0,57,32,82,93,96,3,51,27,36,38,1,19,66,98,93,91,18,95,93,39,12,40,73,100,17,72,93,25,35,45,91,78,13,97,56,40,69,86,69,99,4,36,36,82,35,52,12,46,74,57,65,91,51,41,42,17,78,49,75,9,23,65,44,47,93,84,70,19,22,57,27,84,57,85,2,61,17,90,34,49,74,64,46,61,0,28,57,78,75,31,27,24,10,93,34,19,75,53,17,26,2,41,89,79,37,14,93,55,74,11,77,60,61,2,68,0,15,12,47,12,48,57,73,17,18,11,83,38,5,36,53,94,40,48,81,53,32,53,12,21,90,100,32,29,94,92,83,80,36,73,59,61,43,100,36,71,89,9,24,56,7,48,34,58,0,43,34,18,1,29,97,70,92,88,0,48,51,53,0,50,21,91,23,34,49,19,17,9,23,43,87,72,39,17,17,97,14,29,4,10,84,10,33,100,86,43,20,22,58,90,70,48,23,75,4,66,97,95,1,80,24,43,97,15,38,53,55,86,63,40,7,26,60,95,12,98,15,95,71,86,46,33,68,32,86,89,18,88,97,32,42,5,57,13,1,23,34,37,13,65,13,47,55,85,37,57,14,89,94,57,13,6,98,47,52,51,19,99,42,1,19,74,60,8,48,28,65,6,12,57,49,27,95,1,2,10,25,49,68,57,32,99,24,19,25,32,89,88,73,96,57,14,65,34,8,82,9,94,91,19,53,61,70,54,4,66,26,8,63,62,9,20,42,17,52,97,51,53,19,48,76,40,80,6,1,89,52,70,38,95,62,24,88,64,42,61,6,50,91,87,69,13,58,43,98,19,94,65,56,72,20,72,92,85,58,46,67,2,23,88,58,25,88,18,92,46,15,18,37,9,90,2,38,0,16,86,44,69,71,70,30,38,17,69,69,80,73,79,56,17,95,12,37,43,5,5,6,42,16,44,22,62,37,86,8,51,73,46,44,15,98,54,22,47,28,11,75,52,49,38,84,55,3,69,100,54,66,6,23,98,22,99,21,74,75,33,67,8,80,90,23,46,93,69,85,46,87,76,93,38,77,37,72,35,3,82,11,67,46,53,29,60,33,12,62,23,27,72,35,63,68,14,35,27,98,94,65,3,13,48,83,27,84,86,49,31,63,40,12,34,79,61,47,29,33,52,100,85,38,24,1,16,62,89,36,74,9,49,62,89]))

