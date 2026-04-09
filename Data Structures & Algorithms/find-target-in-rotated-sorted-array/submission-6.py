class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r =0 , n-1

        while l < r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        min_i = l

        if nums[min_i] == target:
            return min_i 
        if min_i == 0:
            l, r = 0, n-1
        
        elif target >= nums[0] and target <= nums[min_i-1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i+1, n-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid+1
            
            else:
                r = mid-1
        return -1
        