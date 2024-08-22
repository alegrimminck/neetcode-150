class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        l, r = 0, 0
        while r < len(nums):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])

            if r + 1 >= k:
                res.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
            r += 1
        return res
