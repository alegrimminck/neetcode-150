class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        d = []
        for s in strs:
            d.append(str(len(s)))
        
        return ",".join(d) + "F" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        for i in range(len(s)):
            if s[i] == "F":
                break
        
        distances, words = [s[:i], s[i+1:]]
        
        res = []
        i = 0
        for n in distances.split(","):
            word = words[i:i+int(n)]
            res.append(word)
            i += int(n)

        return res