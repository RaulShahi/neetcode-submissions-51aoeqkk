class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #bottom up approach
        total = sum(nums)
        if abs(target) > total:
            return 0
        n = len(nums)
        prev = [0] * ((2*total)+1)

        prev[target+total] = 1

        for i in range(n-1, -1, -1):
            curr = [0] * ((2*total)+1)
            for curr_sum in range(-total, total+1, ):
                index = curr_sum + total

                #subtract the element
                if curr_sum - nums[i] >= -total:
                    curr[index] += prev[index - nums[i]]
                if curr_sum + nums[i] <= total:
                    curr[index] += prev[index+ nums[i]]
            prev = curr

        return prev[total]