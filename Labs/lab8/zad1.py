# Zadanie 1. (Pause) Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w Polsce.
# Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które tworza
# spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
# dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu działajacych
# stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm podający
# kolejność wyłączania stacji.

# ROZW: DFS z zapisywaniem czasu przetworzenia

def turn_of(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = [0 for _ in range(n)]
    time = 0

    def DFS(u):
        nonlocal visited, result, time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS(v)
        result[time] = u
        time += 1

    DFS(0)
    return result