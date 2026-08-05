from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left, total, res = 0, 0, 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[left]
                count[f] -= 1
                total -= 1
                left += 1

                if count[f] == 0:
                    del count[f]

            res = max(res, total)
        
        return res


        