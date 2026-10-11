class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #bottom up approach optimized space
        n = len(nums)
        total = sum(nums)
        if total%2 == 1:
            return False
        
        target = total // 2

        prev_row = [False] * (target + 1)
        prev_row[-1] = True

        for i in range(n-1, -1, -1):
            curr_row = [False] * (target+1)

            for curr_sum in range(target+1):
                # skip the item 
                curr_row[curr_sum] = prev_row[curr_sum] 
                # take the item
                if curr_sum + nums[i] <= target:
                    curr_row[curr_sum]= curr_row[curr_sum] or prev_row[curr_sum + nums[i]]
            prev_row = curr_row
        
        return prev_row[0]