class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = {}

        for dest,src in prerequisites:
            graph[src].append(dest)

            indegree[dest] = indegree.get(dest,0)+1
        
        # Queue for maintainig list of nodes that have 0 in-degree

        queue = deque([k for k in range(numCourses) if k not in indegree])

        sorted_order = []

        while queue:
            node = queue.popleft()
            sorted_order.append(node)

            # Reduce in-degree for all the neighbors

            if node in graph:
                for nei in graph[node]:
                    indegree[nei] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[nei] == 0:
                        queue.append(nei)
        return sorted_order if len(sorted_order) == numCourses else []