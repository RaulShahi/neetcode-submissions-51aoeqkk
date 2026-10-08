class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        prev_row = [0] * (capacity + 1)

        for i in range(n-1, -1, -1):
            curr_row = [0] * (capacity+1)
            for c in range(capacity+1):
                #1. skip the item
                curr_row[c] = prev_row[c]

                #2.take the item
                new_capacity = c - weight[i]
                if new_capacity >= 0:
                    p = profit[i] + curr_row[new_capacity]
                    curr_row[c] = max(curr_row[c], p)
            
            prev_row = curr_row
        
        return prev_row[-1]


