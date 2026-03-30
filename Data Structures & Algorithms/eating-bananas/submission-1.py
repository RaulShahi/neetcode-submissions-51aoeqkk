from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxm = max(piles)
        minm =1 
        n = len(piles)
        ans = float("inf")

        def valid(rate):
            hrs = 0
            for banana in piles:
                    hrs += ceil(banana/rate)
            return hrs <= h

        while minm <= maxm:
            mid = (minm + maxm)//2

            if valid(mid):
                ans = min(ans, mid)
                maxm = mid - 1
            else:
                minm = mid + 1
        return ans
                



        
