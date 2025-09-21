class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {
            i: [] for i in range(n)
        }
        for c1, c2 in edges:
            adjMap[c1].append(c2)
            adjMap[c2].append(c1)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adjMap[node]:
                dfs(nei)
        
        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        return components