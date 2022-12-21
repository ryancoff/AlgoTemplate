# 797. All Paths From Source to Target (90.68%)

# Clean solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        if not graph or len(graph) == 0:
            return paths

        queue = deque()
        path = [0]
        queue.append(path)

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            for next_node in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(next_node)

                if next_node == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        return paths

# Good test case
# [[4,1],[2,3,4],[3],[4],[]] (81.93%)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

                # print(f"Node {node} Queue {q}")

        n       =   len(graph)
        adj     =   graph
        paths   =   []
        queue   =   deque()
        path    =   [0]
        queue.append(path)

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            # print(f"Queue {queue} current_path {current_path} ")
            for neighbor in adj[node]: # Traverse Level
                # Each loop add 1 level to current BFS tree 
                temp_path = current_path.copy()
                temp_path.append(neighbor) 
                # print(f"temp_path {temp_path}")
                if neighbor == n-1: 
                    paths.append(temp_path) # Check condition
                else:
                    queue.append(temp_path) # Push New Level to Queue
            # print(f"Queue {queue}")

        return paths