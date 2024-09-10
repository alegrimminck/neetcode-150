class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for p in s:
            if p in pMap:
                stack.append(p)
                continue

            if not stack or pMap[stack.pop()] != p:
                return False
        return not stack
