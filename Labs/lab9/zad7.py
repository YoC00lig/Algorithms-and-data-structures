# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B.
# Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną
# listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak, żeby każda grupka
# mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile (najmniej) grupek przewodnik musi
# podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy dostali się z A do B.

from queue import PriorityQueue
from math import ceil

def TouristGuideProblem(G,a,b,k):
    n = len(G)
    visited = [False] * n
    D = [-1] * n
    P = [None] * n
    q = PriorityQueue()
    visited[a] = True
    D[a] = 0

    q.put((-float("inf"), a))
    while not q.empty():
        weight, vert = q.get()
        weight = -weight
        if vert == b: return ceil(k / D[b])
        for el, w in G[vert]:
            if D[el] < min(weight, w):
                D[el] = min(weight, w)
                P[el] = vert
                q.put((-D[el], el))