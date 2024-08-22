from types import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for n in hashSet:
            if n-1 not in hashSet:
                i = 1
                while n+i in hashSet:
                    i += 1
                longest = max(longest, i)
        return longest
        