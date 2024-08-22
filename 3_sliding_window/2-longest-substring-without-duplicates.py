class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seq = set()
        res = 0

        for c in s:
            while c in seq:
                seq.remove(s[l])
                l += 1
            seq.add(c)
            res = max(res, len(seq))
        return res
            