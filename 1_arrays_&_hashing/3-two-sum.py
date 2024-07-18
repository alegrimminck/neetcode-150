class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in hashNums:
                return [hashNums[nums[i]], i]
            
            hashNums[diff] = i
