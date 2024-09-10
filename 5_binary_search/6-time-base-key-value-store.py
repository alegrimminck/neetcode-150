from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        res = ""
        
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2

            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
