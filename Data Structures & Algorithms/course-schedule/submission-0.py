from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        courses = 0

        for dst, src in prerequisites:
            graph[src].append(dst)

            indegree[dst] += 1
        
        queue = deque([k for k in range(numCourses) if k not in indegree])

        if len(queue) == 0:
            return False
        
        while queue:
            course = queue.popleft()
            courses += 1

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return courses == numCourses

        