# https://leetcode.com/problems/expression-add-operators/

# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
# 
# Examples:
# 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []


# WHAT ARE THE OPTIONS:
# 1) char at 0 * [stuff]
# 2) char at 0 + [stuff]
# 3) char at 0 - [stuff]
# 4) char at 0 concated with char at 1 [stuff]

# I would want a function with: STUFF ON THE LEFT, target?? maybe., stuff on the right
# Re: target. Do we want to have the remainder or target? It seems easiest to evaluate only at the end (once every possibility is placed), so at that point we just need to eval

# ISSUE: how do we pass this? AKA how do we make sure that we don't do ++ in a row?
# ANOTHER WAY WE COULD THINK OF IT: we want to combine two things. (The left and the right). How do we combine them? THEN the issue is...what exactly is the thing to the right? LET'S ASSUME that left and right are always numbers. So what are we doing? We are combining them in one of our four ways.

# BUT: how will we handle the recursion such that the left and right are always numbers? (Or could be evaluated to nums)

# 1+2+3
# 1+2*3
# 1+2-3
# 1+23
# 1*2+3
# 1*2*3
# 1*2-3
# 1*23
# 1-2+3
# 1-2*3
# 1-2-3
# 1-23

# WORKING, but too slow
class Solution:
    def addOperators(self, num, target):
        results = []
        def helperAddOperators(left, right, target):
            if len(right) == 0:
                result = eval(left)
                if result == target:
                    results.append(left)
            else:
                firstNonZeroPos = 0
                while firstNonZeroPos < len(right) and right[firstNonZeroPos] == '0':
                    firstNonZeroPos += 1

                if firstNonZeroPos < len(right):
                    helperAddOperators(left+"+"+right[firstNonZeroPos], right[firstNonZeroPos+1:], target)
                    helperAddOperators(left+"*"+right[firstNonZeroPos], right[firstNonZeroPos+1:], target)
                    helperAddOperators(left+"-"+right[firstNonZeroPos], right[firstNonZeroPos+1:], target)
                helperAddOperators(left+right[0], right[1:], target)

                
        if len(num) > 0:
            helperAddOperators(num[0], num[1:], target)
        return results


sol = Solution()
print(sol.addOperators('123', 6))
print(sol.addOperators('105', 5))
print(sol.addOperators("2147483647",2147483647))

            # If we have a correct
            # if len(right) == 0:
            #     result = eval(left)
            #     if result == target:
            #         results.append(left)

            # If we're partway through, we need to pass to the next. What will we pass? Currently our left is 123, our right is ""...right?
            # WRONG. Our left should be '', our right should be '123'
            # We could pass '1+', '23'
            # How would our next thing make sure it didn't do: 1++23?
            # Because if we are going to tack on an operator, we make sure we pass over a digit (or more) as well. ISSUE: how would we handle the concats? If we're moving things from right to left, does that make sense? What would we move over? Don't think this is the best way. Nah it's still fine. We just move 1 to the left without tacking on an operator. 
            # OKAY IMAGINE INSTEAD, our left is '1', our right is '23'. Does that work better? We could then transition: '1[operator]2', '3', and '12', '3'

        # helperAddOperators("", num, target)
