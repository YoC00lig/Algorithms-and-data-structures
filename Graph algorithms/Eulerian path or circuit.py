def CheckDegs(G):
    n = len(G)
    inD, outD = [0]*n, [0]*n
    begin = end = -1

    for u in range(n):
        for v in G[u]:
            outD[u] += 1
            inD[v] += 1
    # wychodzące - wchodzące == 1: początek sciezki
    # wchodzące - wychodzące == 1: koniec sciezki
    # każdy inny wierzcholek ma miec taka sama ilosc wchodzacych i wychodzacych krawędzi
    for i in range(n):
        if outD[i] - inD[i] == 1:
            if begin >= 0: break
            begin = i
            continue
        if inD[i] - outD[i] == 1:
            if end >= 0: break
            end = i
            continue
        if outD[i] == inD[i]: continue
        else: break

    else:
        if begin*end < 0: return None, [] # nie ma początku lub końca
        elif begin == end == -1: return None, outD # nie ma ani początku ani końca - cykl
        else: return begin, outD # ścieżka
    return -1, []

def Eulerian(G):
    begin, out = CheckDegs(G)
    if not out: return [] # nie ma ani sciezki ani cyklu
    if begin is None: # jest cykl
        for i in range(len(G)):
            if G[i]:
                begin = i
                break
    result = []

    def DFS(u):
        while out[u]:
            out[u] -= 1
            v = G[u][out[u]]
            DFS(v)
        result.append(u)

    DFS(begin)
    result.reverse()
    return result