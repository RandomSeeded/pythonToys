# https://leetcode.com/problems/fraction-to-recurring-decimal/

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in parentheses.
# 
# For example,
# 
#     Given numerator = 1, denominator = 2, return "0.5".
#     Given numerator = 2, denominator = 1, return "2".
#     Given numerator = 2, denominator = 3, return "0.(6)".


# THOUGHTS: how do we know when something is repeating? Answer: we see the same 'division' that we've already seen. This suggests that trying to use the default python division and then stringifying it while identifying any repeated segments is not the way to go about this.
# So how WILL we go about this? By doing it long-division style. If we look at the above examples: 1/2: 0. 10 / 2: 5, remainder 0, done, put the dot in the right place
# 2/1 2, remainder 0, done
# 2/3 0, 20 / 3: 6, remainder 2, 2/3, SEEN BEFORE. Note: we'll need to keep track of where we saw it before so that we know where to put the parens
# 22/3: 7, remainder 1, 1/3 0, 10/3: 3, remainder 1, seen before


# Remaining issues: proper decimal handling for non-zero cases

import math
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        # Key-values: numerator, start position in solution
        seen = {}

        def helperFractionToDecimal(numerator, result):
            # Keep track of adding decimal
            first = result == ""

            dividend = int(numerator / denominator)
            if numerator in seen:
                # print('put opening parens at',seen[numerator])
                result = result[:seen[numerator]] + "(" + result[seen[numerator]:]+")"
                return result
            else:
                seen[numerator] = len(result)

            remainder = numerator % denominator

            if dividend == 0:
                # if result == "":
                #     result += "0."
                # else:
                result += "0"
            else:
                result += str(dividend)

            if first and remainder != 0:
                result += "."
            if remainder == 0:
                return result
            else: 
                result = helperFractionToDecimal(int(str(remainder) + "0"), result)
                return result

        result = helperFractionToDecimal(numerator,"")
        return result
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
sol = Solution()
print(sol.fractionToDecimal(2,3))
print(sol.fractionToDecimal(2,1))
print(sol.fractionToDecimal(1,11))
print(sol.fractionToDecimal(1,5))
print(sol.fractionToDecimal(22,7))
print(sol.fractionToDecimal(-50, 8))
