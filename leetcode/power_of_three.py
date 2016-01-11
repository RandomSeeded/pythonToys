#https://leetcode.com/problems/power-of-three/

#  Given an integer, write a function to determine if it is a power of three.
#  
#  Follow up:
#  Could you do it without using any loop / recursion? 

# WITH RECURSION
class Solution:
    def isPowerOfThree(self, n):
        if n > 3:
            return self.isPowerOfThree(n / 3)
        elif n == 3:
            return True
        else:
            return False

# thoughts on doing it WITHOUT a loop or recursion?
# aka other ways we can handle this:
# what makes something a power of 3? It's ONLY factors are 3
# One other way we could do this would be check to see if there were any other factors, but that would require a loop as well



sol = Solution()
print(sol.isPowerOfThree(2))
print(sol.isPowerOfThree(3))
print(sol.isPowerOfThree(9))
print(sol.isPowerOfThree(12))
