"""TODO"""
from kol2atesty import runtests

def prepareTab(P):
    new = []
    n = len(P)
    for i in range(n): new.append([P[i][0], P[i][1], i])
    new.sort()

    res = []
    cnt = 0
    for i in range(n):
        if not new[i][1]: cnt += 1# punkt kontrolny
        else:
            res.append([new[i][0], cnt, new[i][2]])
            cnt = 0
    return res

def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje
    return []

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )