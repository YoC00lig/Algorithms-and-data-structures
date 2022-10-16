# Wykonujemy DFS, usuwając na bieżąco krawędzie po których wędrujemy
# po przetworzeniu wierzchołka dodajemy go na początek tworzonego cyklu

def EulerCycle(G):
    stack = []
    result = []

    def DFS(u):
        nonlocal G, stack

        for i in G[u]:
            G[u].remove(i)
            G[i].remove(u)
            stack.append(i)
            DFS(i)
        if len(G[u]) == 0:
            result.append(stack.pop())

    for v in range(len(G)):
        if len(G[v]) > 0:
            stack.append(v)
            DFS(v)

    return result

