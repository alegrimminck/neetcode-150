from types import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        first = nums[0]
        second = fast

        while True:
            if first == second:
                return first

            first = nums[first]
            second = nums[second]
