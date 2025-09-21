class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {
            i: [] for i in range(numCourses)
        }
        for course,pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()

        def dfs(course):
            if preMap[course] == None:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for nei in preMap[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            preMap[course] = None
            res.append(course)
            return True
        
        res = []
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res