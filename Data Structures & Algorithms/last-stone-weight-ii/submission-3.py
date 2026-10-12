class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #bottom up approach
        sumStones = sum(stones)
        n = len(stones)
        target = math.ceil(sumStones/2)
        
        prev = [0] * (target+1)

        for j in range(target + 1):
            prev[j] = abs(j - (sumStones - j))

        for i in range(n-1, -1, -1):
            curr = [0] * (target+1)
            for j in range(target + 1):
                # skip
                curr[j] = prev[j]

                #take
                if j + stones[i] <= target:
                    take = prev[j+stones[i]]
                    curr[j] = min(take, curr[j])
            prev = curr
        
        return prev[0]