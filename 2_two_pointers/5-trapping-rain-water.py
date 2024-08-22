from types import List

class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        postfix = [0]

        for i in range(1, len(height)):
            if height[i-1] > prefix[-1]:
                prefix.append(height[i-1])
            else:
                prefix.append(prefix[-1])
            
            if height[-i] > postfix[-1]:
                postfix.append(height[-i])
            else:
                postfix.append(postfix[-1])
        postfix.reverse()

        res = 0
        for i in range(len(height)):
            smallerWall = min(prefix[i], postfix[i])
            currentHeight = height[i]
            res += max(smallerWall - currentHeight, 0)
        
        return res
