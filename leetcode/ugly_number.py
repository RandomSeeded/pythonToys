# https://leetcode.com/problems/ugly-number/

#  Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# 
# Note that 1 is typically treated as an ugly number. 

# Easiest way to do this: factorize the number. If at any point in time you come across a factor that isn't 2/3/5, ret 

import math
class Solution:
    def isUgly(self, num):
        uglyFactors = {2: True, 3: True, 5: True}
        def factorize(number):
            if number == 1:
                return True
            for i in range(2, int(math.floor(number / 2)+1)):
                remainder = number % i
                if remainder == 0:
                    if i not in uglyFactors:
                        return False
                    return factorize(int(number / i))

            if number not in uglyFactors:
                return False
            return True

        return factorize(num)


sol = Solution()
print(sol.isUgly(214797179))
print(sol.isUgly(14))
print(sol.isUgly(6))
print(sol.isUgly(8))
