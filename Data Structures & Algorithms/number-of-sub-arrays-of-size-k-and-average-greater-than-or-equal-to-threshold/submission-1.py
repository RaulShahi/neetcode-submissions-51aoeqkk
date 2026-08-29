class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        ans = 0

        for i in range(k):
            total += arr[i]
        
        ans += total >= threshold * k

        for i in range(k, len(arr)):
            total += arr[i] - arr[i-k]
            ans += total >= threshold * k
        
        return ans
        