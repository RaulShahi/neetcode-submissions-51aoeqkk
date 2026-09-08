class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = -1
        prefix = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        
        for i in range(len(nums)):
            if i == 0:
                if prefix[-1] - prefix[0] == 0:
                    return 0
            if prefix[i-1] == prefix[-1] - prefix[i]:
                return i 

        return index
        