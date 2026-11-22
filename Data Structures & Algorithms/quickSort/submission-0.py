# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort(pairs,0,len(pairs)-1)
        return pairs
    
    def sort(self, pairs,s, e):
        if e-s+1 <= 1:
            return pairs
        
        pivot = pairs[e]
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1
        pairs[e], pairs[left] = pairs[left], pairs[e]

        self.sort(pairs, s, left-1)
        self.sort(pairs, left+1, e)
    
    
        