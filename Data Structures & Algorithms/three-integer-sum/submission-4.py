class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = nums[i]
            j = i+1
            k = len(nums)-1


            while j < k:
                sum_ = curr + nums[j] + nums[k]
                if sum_ == 0:
                    ans.append([curr, nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
                
                elif sum_ > 0:
                    k -= 1
                else:
                    j += 1
        return ans
                
        