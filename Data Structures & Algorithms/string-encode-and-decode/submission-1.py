class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            length = str(len(word))
            res += length + "#" + word
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i <(len(s)):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j+length +1
            
        return res

