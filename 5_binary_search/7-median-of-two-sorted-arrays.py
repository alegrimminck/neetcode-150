from types import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            mB = half - m - 2

            leftA = A[m] if m >= 0 else float("-inf")
            rightA = A[m+1] if (m + 1) < len(A) else float("inf")
            leftB = B[mB] if mB >= 0 else float("-inf")
            rightB = B[mB+1] if (mB + 1) < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                # odd
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = m - 1
            else:
                l = m + 1
