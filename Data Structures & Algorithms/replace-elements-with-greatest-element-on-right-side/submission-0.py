class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxRight = arr[n - 1]

        for i in range(n-2, -1, -1):
            tmp = arr[i]
            arr[i] = maxRight
            maxRight = max(maxRight, tmp)
        
        arr[n-1] = -1
        return arr

        