class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preProduct = [1] * n
        postProduct = [1] * n
        ans = []

        for i in range(1, n):
            preProduct[i] = preProduct[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            postProduct[i] = postProduct[i+1] * nums[i+1]
        
        print(preProduct)
        print(postProduct)
        
        for i in range(n):
            ans.append(preProduct[i]*postProduct[i])
        
        return ans

        