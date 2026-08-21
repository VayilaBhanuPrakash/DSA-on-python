class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]

        for r,c in edges:
            graph[r].append(c)
            graph[c].append(r)

        
        visited = [False] * n
        next = []
        next.append(source)

        visited[source] = True

        i  = 0

        while i <= len(next) -1:
            curr = next[i]
            if curr == destination:
                return True
            for j in graph[curr]:
                if visited[j] == False:
                    visited[j] = True
                    next.append(j)
            i += 1
        return False
        