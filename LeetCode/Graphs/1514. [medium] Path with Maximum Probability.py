"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.


"""
from queue import PriorityQueue
from math import log2,inf,e
def maxProbability(n,edges, succProb, start,end):
    G = [[] for _ in range(n)]

    for i in range(len(edges)):
        idx1, idx2, cost = edges[i][0], edges[i][1], succProb[i]
        G[idx1].append([idx2, log2(1 / cost)])
        G[idx2].append([idx1, log2(1 / cost)])

    D = [inf] * n
    q = PriorityQueue()
    q.put((0, start))

    while not q.empty():
        weight, u = q.get()
        if weight < D[u]:
            D[u] = weight
            if u == end: break

            for [v, w] in G[u]:
                if D[v] == inf:
                    q.put((D[u] + w, v))

    if D[end] == inf:
        return 0
    else:
        return 1 / (2 ** D[end])