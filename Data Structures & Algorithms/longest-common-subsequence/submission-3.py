from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        memo = defaultdict(int)

        def dfs_helper(s1, s2, i1, i2):
            #base case
            if i1 >= l1 or i2 >= l2:
                return 0
            
            if (i1, i2) not in memo:

                # case matches
                if s1[i1] == s2[i2]:
                    memo[(i1, i2)] =  1 + dfs_helper(s1, s2, i1+1, i2+1)
                
                else:
                    memo[(i1, i2)] = max(dfs_helper(s1, s2, i1+1,i2), 
                                        dfs_helper(s1, s2, i1, i2+1))
                
            return memo[(i1, i2)]
        
        return dfs_helper(text1, text2, 0, 0)

