from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)

        for word in strs:
            collection["".join(sorted(word))].append(word)
        
        return [val for val in collection.values()]

        