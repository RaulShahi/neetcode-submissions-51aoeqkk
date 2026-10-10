class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Bottomup optimized space
        n, m = len(text1), len(text2)

        prev_row = [0] * (m+1)

        for i in range(n-1, -1, -1):
            curr_row = [0] * (m+1)
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    curr_row[j] = 1 + prev_row[j+1]
                
                else:
                    curr_row[j] = max(prev_row[j], curr_row[j+1])

            prev_row = curr_row
        
        return prev_row[0]
        