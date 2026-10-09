class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        prev_row = [0] * (capacity+1)

        for i in range(n-1, -1, -1):
            curr_row = [0] * (capacity+1)

            for c in range(capacity + 1):
                #skip 
                curr_row[c] = prev_row[c]

                #take 
                new_capacity = c - weight[i]
                if new_capacity >= 0:
                    curr_row[c] = max(curr_row[c], profit[i]+prev_row[new_capacity])
            
            prev_row = curr_row
        
        return prev_row[-1]
