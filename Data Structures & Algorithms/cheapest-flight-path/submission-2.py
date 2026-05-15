#Bellman ford algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float("inf")
        dp = [inf]*n

        dp[src] = 0

        for _ in range(k+1):
            temp = dp[:]

            for u, v, cost in flights:
                if dp[u] != inf:
                    temp[v] = min(temp[v], dp[u]+cost)
            dp = temp
        
        return -1 if dp[dst] == inf else dp[dst]
            
        