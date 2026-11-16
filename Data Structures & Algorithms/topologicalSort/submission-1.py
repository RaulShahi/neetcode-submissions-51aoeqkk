from collections import deque, defaultdict
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([k for k in range(n) if k not in indegree])

        if len(queue) == 0:
            return []
        
        tp_list = []

        while queue:
            node = queue.popleft()
            tp_list.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return tp_list if len(tp_list) == n else []

        

        