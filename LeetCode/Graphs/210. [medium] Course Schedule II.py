"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want
to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return
any of them. If it is impossible to finish all courses, return an empty array.
"""

def findOrder(n,p):
    def has_cycle(G):
        visited = [False] * n

        def cycle(u):
            nonlocal visited
            if visited[u]:
                return True
            else:
                visited[u] = True
            for v in G[u]:
                if cycle(v): return True
            visited[u] = False
            return False

        for u in range(len(G)):
            if cycle(u): return False
        return True

    G = [[] for _ in range(n)]
    for a, b in p: G[b].append(a)

    def Topo(G):
        nonlocal n
        visited = [False] * n
        res = [-1] * n
        i = n - 1

        def DFS(u):
            nonlocal visited, res, i
            visited[u] = True
            for v in G[u]:
                if not visited[v]: DFS(v)
            res[i] = u
            i -= 1

        for w in range(n):
            if not visited[w]: DFS(w)

        return res

    can = has_cycle(G)
    x = []
    if can: x = Topo(G)
    return x