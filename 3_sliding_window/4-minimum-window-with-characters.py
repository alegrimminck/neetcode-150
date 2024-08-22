class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT, countS = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        
        l, r = 0, 0
        resLength = float("inf")
        res = [0, 0]
        while r < len(s):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            r += 1

            while have == need:
                if (r - l + 1) < resLength:
                    resLength = (r - l + 1)
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] == countT[s[l]] - 1:
                    have -= 1
                l += 1
        
        if resLength == float("inf"):
            return ""
        l, r = res
        return s[l:r]
        