from types import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float("inf")
        
        while l <= r:
            k = (l + r) // 2

            hours = 0
            for b in piles:
                hours += math.ceil(b / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
