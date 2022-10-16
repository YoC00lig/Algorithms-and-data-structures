# Zadanie 2. (uniwersalne ujście) Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym ujściem,
# jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
# wychodząca z t.

# 1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n2)).

def UniversalPath(G):
    n = len(G)

    for i in range(n):
        cnt = 0
        for j in range(n): # zliczanie ile wierzchołków ma krawędź do sprawdzanego wierzchołka ad. a)
            if G[j][i] == 1 and i != j:
                cnt += 1
        if cnt == n - 1: # jeśli wszystkie maja krawędz, to sprawdzamy czy z tego wierzchołka nie wychodzi żadna krawędź ad. b)
            for j in range(n):
                if i != j and G[i][j] == 0:
                    cnt -= 1
            if cnt == 0: return i
    return None

# 2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.

def IsUniversal(i,G): # sprawdza czy wierzchołek jest uniwersalnym ujściem
    n = len(G)
    for j in range(n):
        if G[i][j] == 1: return False
        if G[j][i] == 0 and i != j: return False
    return True

def UniversalPath2(G):
    i,j = 0, 0
    n = len(G)

    while i < n and j < n:
        if G[i][j] == 0:
            j += 1
        elif G[i][j] == 1:
            i += 1

    if i > n or not IsUniversal(i,G): return None
    return i