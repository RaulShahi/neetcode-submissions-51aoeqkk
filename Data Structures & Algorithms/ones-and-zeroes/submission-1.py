from collections import defaultdict
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        #Find number of zeros and ones in each string
        def helper(str):
            ones, zeros = 0,0

            for ch in str:
                if ch == "0":
                    zeros += 1
                
                else:
                    ones += 1
            return zeros, ones
        
        memo = defaultdict(int)
        
        def dfs_helper(i, curr_zeros, curr_ones):
            #base cases
            if i == len(strs):
                return 0
            
            if (i, curr_zeros, curr_ones) not in memo:
            
                #skip the element
                skip = dfs_helper(i+1, curr_zeros, curr_ones)
                memo[(i, curr_zeros, curr_ones)] = skip

                #take the element
                new_zeros, new_ones = helper(strs[i])
                if curr_zeros + new_zeros <= m and curr_ones + new_ones <= n:
                    take = 1 + dfs_helper(i+1, curr_zeros+new_zeros, curr_ones+new_ones)
                    memo[(i, curr_zeros, curr_ones)] = max(skip, take)
            
            return memo[(i, curr_zeros, curr_ones)]

        return dfs_helper(0,0,0) 
        