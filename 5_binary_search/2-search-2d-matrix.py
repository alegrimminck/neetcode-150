from types import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, down = 0, len(matrix) - 1

        while top <= down:
            m = (top + down) // 2
            if matrix[m][0] > target:
                down = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                arr = matrix[m]

                l, r = 0, len(arr) - 1
                while l <= r:
                    m = (l + r) // 2
                    if arr[m] > target:
                        r = m - 1
                    elif arr[m] < target:
                        l = m + 1
                    else:
                        return True
                return False
        return False
