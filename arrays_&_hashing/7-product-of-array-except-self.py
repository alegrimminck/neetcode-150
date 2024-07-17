class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i-1])

        postfix = [1]
        for i in range(len(nums)-2, -1, -1):
            postfix.append(postfix[-1] * nums[i+1])
        postfix.reverse()

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        
        return res
        