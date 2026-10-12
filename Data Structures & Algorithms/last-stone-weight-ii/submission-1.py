from heapq import *
from collections import defaultdict
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStones = sum(stones)
        target = math.ceil(sumStones/2)

        memo = defaultdict(int)

        def dfs(i, total):
            #base cases
            if total > target or i == len(stones):
                # subtracting the other half
                return abs(total - (sumStones - total))
            
            if (i, total) not in memo:
                #skip
                skip = dfs(i+1, total)

                #take 
                take = dfs(i+1, total + stones[i])

                memo[(i, total)] = min(skip, take)

            return memo[(i,total)]

        return dfs(0, 0)            
        