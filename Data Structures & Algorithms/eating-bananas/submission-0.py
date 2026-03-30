from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(mid):
            hrs = 0
            for p in piles:
                hrs += ceil(p/mid)
            return hrs <= h

        minm = 1
        maxm = max(piles) #O(n)
        ans = float("inf")

        while minm <= maxm:
            mid = (minm+maxm)//2

            if check(mid):
                ans = min(ans, mid)
                maxm = mid-1
            else:
                minm = mid + 1
        
        return ans




        