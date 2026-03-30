class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        def numOnes(n):
            cnt = 0
            while n:
                n &= n-1
                cnt += 1
            return cnt

        for i in range(1,n+1):
            ans.append(numOnes(i))
        
        return ans

        