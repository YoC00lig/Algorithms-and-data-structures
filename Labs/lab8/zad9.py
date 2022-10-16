# Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
# ma koszt (liczbę ze zbioru {1,...,5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym
# rogu szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac
# po polach o minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A),
# która oblicza koszt sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.


# wkładanie wartości kilka razy do kolejki

from queue import PriorityQueue
from math import inf

def KingsPath(G):
    n = len(G)
    dist = [[inf]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    q = PriorityQueue()
    q.put((G[0][0], 0, 0))
    visited[0][0] = True
    dist[0][0] = G[0][0]

    while not q.empty():
        dist, row, col = q.get()
        visited[row][col] = True

        new_row = [row + 1, row + 1, row, row - 1, row - 1, row - 1, row, row + 1]
        new_col = [col, col + 1, col + 1, col + 1, col, col - 1, col - 1, col - 1]

        for i in range(len(new_col)):
            if 0 <= new_row[i] < len(G) and 0 <= new_col[i] < len(G):
                currRow, currCol = new_row[i], new_col[i]
                if not visited[currRow][currCol]:
                    if dist[currRow][currCol] > dist[row][col] + G[currRow][currCol]:
                        dist[currRow][currCol] = dist[row][col] + G[currRow][currCol]
                        q.put((dist[currRow][currCol], currRow, currCol))

    return dist[-1][-1]