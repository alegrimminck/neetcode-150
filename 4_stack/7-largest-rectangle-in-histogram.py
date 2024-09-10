from types import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        l, r = 0, 0
        while l < len(heights):
            minHeight = heights[l]

            while r < len(heights) and heights[r] != 0:
                minHeight = min(minHeight, heights[r])
                area = minHeight  * ( r - l + 1 )
                maxArea = max(maxArea, area)
                r += 1

            l += 1
            r = l
        return maxArea
