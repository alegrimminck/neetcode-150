class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n-1:
            return False

        preMap = {
            i: [] for i in range(n)
        }
        for c1, c2 in edges:
            preMap[c1].append(c2)
            preMap[c2].append(c1)
        
        visited = set()

        q = deque([(None, 0)]) # Parent, node
        while q:
            parent, curr = q.popleft()
            for nei in preMap[curr]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                
                visited.add(nei)
                q.append((curr, nei))
        return True
