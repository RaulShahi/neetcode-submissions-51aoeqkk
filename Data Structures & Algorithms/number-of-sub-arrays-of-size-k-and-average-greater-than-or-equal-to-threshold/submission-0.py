class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = 0
        ans = 0

        def check(summ):
            return 1 if summ/k >= threshold else 0

        for i in range(k):
            summ += arr[i]
        

        ans += check(summ)
        for i in range(k, len(arr)):
            summ += arr[i] - arr[i-k]
            print(summ, summ/k)
            ans += check(summ)
        
        return ans


        