from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #edge cases
        if n<=2:

            return [i for i in range(n)]
        graph = defaultdict(list)

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        leaves = []

        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n
        
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()

                #remove the only neighbor
                nei = graph[leaf].pop()

                graph[nei].remove(leaf)

                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            
            leaves = new_leaves
        return leaves
        

        