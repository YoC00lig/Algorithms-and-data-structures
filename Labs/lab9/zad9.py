# Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróżnik chce przebyć trasę z punktu A do punktu B.
# Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie
# D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to łączące je
# drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym wierzchołku jest
# stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z punktu A do punktu B
# o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.

from math import inf
from queue import PriorityQueue

def MinCost(G, A, B, D, C, StartFuel):
    n = len(G)
    F = [[inf] * (D+1) for _ in range(n)] # koszt dojechania do wierzchołka i mając x benzyny wyjeżdżajac z poprzedniego wierzchołka
    P = [[None] * (D+1) for _ in range(n)]
    q = PriorityQueue()
    q.put((0, StartFuel, 0, A, None))
    end = False

    while not q.empty():

        cost, fuel, prev_fuel, vert, parent = q.get()

        if cost < F[vert][fuel]:
            F[vert][fuel] = cost
            P[vert][fuel] = (parent, prev_fuel)

            if vert == B:
                end = fuel
                break

            for v, dist in G[vert]:
                for refueled in range(max(0, dist - fuel), D - fuel+1):
                    new = fuel + refueled
                    if F[v][new] == inf:
                        q.put( (cost + refueled*C[vert], new - dist, fuel, v, vert) )


    return F,P,end if end else None,None,None


def GetPath(P,B,end):

    path = [B]
    x = P[B][end]

    while True:
        B, fuel = x
        if B is None: break
        path.append(B)
        x = P[B][fuel]

    path.reverse()
    return path

    