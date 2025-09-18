class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = []
        for val in counts.values():
            heapq.heappush(maxHeap, -val)
        
        q = deque()
        time = 0
        while q or maxHeap:
            if maxHeap:
                popped = heapq.heappop(maxHeap)
                if popped < -1:
                    q.append((popped+1, time+n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
            time += 1
        return time

                