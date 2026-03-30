class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        def backtrack(curr, total, i):
            if total > target or i > n:
                return
            
            if total == target:
                ans.append(curr[:])
            
            for j in range(i, n):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                backtrack(curr, total+candidates[j], j+1)
                curr.pop()
            
        
        ans = []
        backtrack([], 0, 0)
        return ans
        