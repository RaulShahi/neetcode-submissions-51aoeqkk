from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = Counter(s)

        for c in t:
            if c not in s_count or s_count[c] == 0:
                return False
            s_count[c] -= 1
        
        return True
        
        