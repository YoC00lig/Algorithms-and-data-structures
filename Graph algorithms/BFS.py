from collections import deque

def BFS(G, start):
    n = len(G)
    visited = [False] * n
    queue = deque([])
    visited[start] = True
    queue.append(start)

    while queue:
        u = queue.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
