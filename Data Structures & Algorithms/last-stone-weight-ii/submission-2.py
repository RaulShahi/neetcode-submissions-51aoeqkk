class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #bottom up approach
        
        sumStones = sum(stones)
        n = len(stones)
        target = math.ceil(sumStones/2)
        
        memo = [[0] * (target+1) for _ in range(n+1)]

        for j in range(target + 1):
            memo[n][j] = abs(j - (sumStones - j))

        for i in range(n-1, -1, -1):
            for j in range(target + 1):
                # skip
                memo[i][j] = memo[i+1][j]

                #take
                if j + stones[i] <= target:
                    take = memo[i+1][j+stones[i]]
                    memo[i][j] = min(take, memo[i][j])
        
        return memo[0][0]