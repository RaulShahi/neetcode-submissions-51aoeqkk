class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #bottom up approach
        n = len(nums)
        total = sum(nums)
        if total%2 == 1:
            return False
        
        target = total // 2
        memo = [[False] * (target+1) for i in range(n+1)]

        #no items remaining, target already reached
        memo[n][target]= True

        for i in range(n-1, -1, -1):
            for j in range(target+1):
                
                #skip the item
                memo[i][j] = memo[i+1][j]

                #take the item
                if j + nums[i] <= target:
                    memo[i][j] = memo[i][j] or memo[i+1][j+nums[i]]
        
        return memo[0][0]

        