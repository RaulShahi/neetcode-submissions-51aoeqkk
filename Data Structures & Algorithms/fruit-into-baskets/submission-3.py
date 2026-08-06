from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l, ans = 0,0

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1

                if count[f] == 0:
                    del count[f]
                
                l += 1
            
            ans = max(ans, r - l +1)
        
        return ans

        