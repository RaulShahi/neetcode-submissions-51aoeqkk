class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = [[[0]*(n+1) for _ in range (m+1)] for _ in range(len(strs)+1)]
                #Find number of zeros and ones in each string
        def helper(str):
            ones, zeros = 0,0

            for ch in str:
                if ch == "0":
                    zeros += 1
                
                else:
                    ones += 1
            return zeros, ones
        
        for i in range(len(strs)-1,-1,-1):
            for curr_zeros in range(m+1):
                for curr_ones in range(n+1):
                    #skip the element
                    skip = memo[i+1][curr_zeros][curr_ones]
                    memo[i][curr_zeros][curr_ones] = skip

                    #take the element
                    new_zeros, new_ones = helper(strs[i])
                    if curr_zeros + new_zeros <= m and curr_ones + new_ones <= n:
                        take = 1 + memo[i+1][curr_zeros+new_zeros][curr_ones+new_ones]
                        memo[i][curr_zeros][curr_ones] = max(skip, take)
        
        return memo[0][0][0]
