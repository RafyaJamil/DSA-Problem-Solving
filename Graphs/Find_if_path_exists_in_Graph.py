# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for i in range(n):
            graph[i] = []
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        queue = deque([source])
        while(queue):
            node = queue.popleft()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for neighbour in graph[node]:
                queue.append(neighbour)
        return False

s = Solution()
print(s.validPath(3,[[0,1],[1,2]],0,3))
            