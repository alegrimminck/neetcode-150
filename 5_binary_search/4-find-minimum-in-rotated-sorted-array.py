from types import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = float("inf")

        while l <= r:
            m = (l + r) // 2

            minimum = min(minimum, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return minimum
