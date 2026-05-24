class Solution:
    def climbStairs(self, n: int) -> int:
        backOne = 1
        backTwo = 1

        for i in range(2, n+1):
            temp = backOne + backTwo
            backTwo = backOne
            backOne = temp
        
        return backOne
        