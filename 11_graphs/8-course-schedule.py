class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {
            i: [] for i in range(numCourses)
        }
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()
        
        def dfs(course):
            if len(preMap[course]) == 0:
                return True

            if course in visited:
                return False
            
            visited.add(course)
            for nei in preMap[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True