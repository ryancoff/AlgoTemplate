# 785. Is Graph Bipartite?

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Traverse Neighbor of node 'source'
        def bfs(source):
            q = deque([source])
            color[source] = 0
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == color[node]: 
                        # print(f"neighbor: {neighbor} & node {node}")
                        return False
                    if color[neighbor] == -1: 
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
            return True

        
        n = len(graph)
        color = [-1]*(n)
        # if len
        for i in range(n):
            # [[]] or [[],...]
            # if not graph[i]:
            #     continue
            if color[i] == -1:
                if not bfs(i):
                    return False
            
        return True
