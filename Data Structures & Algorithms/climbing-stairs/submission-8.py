class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        backOne, backTwo = 1, 2

        for i in range(3, n+1):
            tmp = backTwo
            backTwo = backTwo + backOne
            backOne = tmp
        
        return backTwo
        