class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        globalvisited=set()
        provinces = 0
        adj={i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if isConnected[i][j]==1:
                    adj[i].append(j)
       
        for i in range(n):
            if i in globalvisited:
                continue
            globalvisited.add(i)
            stack=[i]
            components=[]
            while stack:
                current=stack.pop()
                for neighbour in adj[current]:
                    if neighbour not in globalvisited:
                        globalvisited.add(neighbour)
                        stack.append(neighbour)
            provinces+=1
        return provinces