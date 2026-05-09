class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float("inf")

        dp = [[inf] * n for _ in range(k+2)]
        #dp[i][v] - minimum price to reach city v with exactly i flights
        dp[0][src] = 0

        for i in range(1, k+2):
            for u,v,price in flights:
                if dp[i-1][u] != inf:
                    dp[i][v] = min(dp[i][v], dp[i-1][u]+price)
        
        ans = min(dp[i][dst] for i in range(k+2))

        return ans if ans != inf else -1
        