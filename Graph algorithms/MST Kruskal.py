def KRUSKAL(G):
    V = len(G)
    parent = [i for i in range(V)]
    rank = [0]*V

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        a = find(x)
        b = find(y)
        if rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b
            if rank[a] == rank[b]:
                rank[b] += 1
    E = []
    # lista sąsiedztwa na listę krawędzi
    for i in range(V):
        for j, val in G[i]: E.append([i, j, val])
    E = sorted(E, key= lambda weight: weight[2])

    A = []
    for e in E:
        if find(e[0]) != find(e[1]):
            A.append(e)
            union(e[0], e[1])
    return A