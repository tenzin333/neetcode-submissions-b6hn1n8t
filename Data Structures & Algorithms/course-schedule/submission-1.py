class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}

        visited = set()

        for cr, pr in prerequisites:
            preMap[cr].append(pr)

        def dfs(cr):
            if cr in visited:
                return False
            
            visited.add(cr)

            for pr in preMap[cr]:
                if not dfs(pr):
                    return False
            visited.remove(cr)
            preMap[cr] = []
            return True
        
        for cr in range(numCourses):
            if not dfs(cr):
                return False
        return True
