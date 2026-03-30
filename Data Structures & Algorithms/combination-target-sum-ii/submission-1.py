class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(curr, sum_,i):
            if sum_ > target:
                return
            if sum_ == target:
                if curr not in ans:
                    ans.append(curr[:])
                return
            
            for j in range(i,len(candidates)):
                sum_ += candidates[j]
                curr.append(candidates[j])
                backtrack(curr, sum_, j+1)
                curr.pop()
                sum_ -= candidates[j]
        
        ans = []
        backtrack([],0,0)
        return ans
        