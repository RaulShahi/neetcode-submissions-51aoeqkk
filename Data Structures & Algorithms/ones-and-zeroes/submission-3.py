class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        prev_grid = [[0]*(n+1) for _ in range(m+1)]
                #Find number of zeros and ones in each string
        def helper(str):
            ones, zeros = 0,0

            for ch in str:
                if ch == "0":
                    zeros += 1
                
                else:
                    ones += 1
            return zeros, ones
    
        for i in range(len(strs)-1, -1, -1):
            curr_grid = [[0]*(n+1) for _ in range (m+1)]
            new_zeros, new_ones = helper(strs[i])
            for curr_zeros in range(m+1):
                for curr_ones in range(n+1):
                    #skip the element
                    skip = prev_grid[curr_zeros][curr_ones]
                    curr_grid[curr_zeros][curr_ones] = skip

                    #take the element
                    if curr_zeros + new_zeros <= m and curr_ones + new_ones <= n:
                        take = 1 + prev_grid[curr_zeros+new_zeros][curr_ones+new_ones]
                        curr_grid[curr_zeros][curr_ones] = max(skip, take)
            prev_grid = curr_grid
        
        return prev_grid[0][0]  