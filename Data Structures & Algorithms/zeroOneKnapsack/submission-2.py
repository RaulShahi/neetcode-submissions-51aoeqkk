class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # using bottom up dynamic programming
        n = len(profit)
        prev_row = [0] * (capacity + 1)

        for i in range(n-1, -1, -1):
            curr_row = [0] * (capacity+1)
            for c in range(1, capacity+1):
                #skip the item
                curr_row[c] = prev_row[c]

                #take the item
                if weight[i] <= c:
                    p = profit[i] + prev_row[c - weight[i]]
                    curr_row[c] = max(curr_row[c], p)
            prev_row = curr_row
        return prev_row[-1]