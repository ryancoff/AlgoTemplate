# 1971. Find if Path Exists in Graph (92.57%)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Traverse All Neighbor of node 'Source'
        def bfs(source, destination):
            q = deque([source])
            visited[source] = 0

            while q:
                # print(f"q: {q}")
                node = q.popleft()
                for neighbor in adj[node]:
                    if neighbor == destination: return True
                    if visited[neighbor] == -1:
                        visited[neighbor] = 0
                        q.append(neighbor)
            return False
    
        if len(edges) == 0:
            return True
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [-1] * n

        for neighbor in adj[source]:
            if visited[neighbor] == -1:
                if bfs(neighbor,destination):
                    return True

        return False


'''

edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
n = 6

q: deque([1])
q: deque([0, 2])
q: deque([2])
q: deque([3])
q: deque([4])

'''