from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')] += 1
            map[tuple(count)].append(word)
        
        return list(map.values())

        