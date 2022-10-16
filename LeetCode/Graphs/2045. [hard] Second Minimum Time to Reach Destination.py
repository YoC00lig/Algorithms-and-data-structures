"""
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
"""

from queue import PriorityQueue


def secondMinimum(n,edges,time,change):
    D = [[] for _ in range(n + 1)]
    D[1] = [0]
    q = PriorityQueue()
    G = [[] for _ in range(n + 1)]

    for a, b in edges:
        G[a].append(b)
        G[b].append(a)

    q.put((0, 1))

    while not q.empty():
        mindist, u = q.get()

        if u == n and len(D[u]) == 2: return max(D[n])

        for v in G[u]:
            if (mindist // change) % 2 == 0:
                curr = mindist + time

            else:
                curr = mindist + time + change - (mindist % change)
            if not D[v] or (len(D[v]) == 1 and D[v] != [curr]):
                D[v].append(curr)
                q.put((curr, v))
