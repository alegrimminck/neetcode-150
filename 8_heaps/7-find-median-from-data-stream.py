class MedianFinder:

    def __init__(self):
        self.smallest = []
        self.largest = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallest, -num)

        if self.largest and -self.smallest[0] > self.largest[0]:
            popped = heapq.heappop(self.smallest)
            heapq.heappush(self.largest, -popped)

        if len(self.smallest)-1 > len(self.largest):
            popped = heapq.heappop(self.smallest)
            heapq.heappush(self.largest, -popped)
        if len(self.largest)-1 > len(self.smallest):
            popped = heapq.heappop(self.largest)
            heapq.heappush(self.smallest, -popped)
        

    def findMedian(self) -> float:
        total = len(self.smallest) + len(self.largest)
        if total % 2:
            if len(self.smallest) > len(self.largest):
                return -self.smallest[0]
            else:
                return self.largest[0]
        return (-self.smallest[0] + self.largest[0])/2
        