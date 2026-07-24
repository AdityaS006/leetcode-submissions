class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        if source == destination:
            return True

        queue=deque()
        queue.append(source)
        visited=set()
        visited.add(source)

        while queue:
            current = queue.pop()

            for neighbour in adj[current]:
                if neighbour in visited:
                    continue
                if neighbour == destination:
                    return True
                else:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False