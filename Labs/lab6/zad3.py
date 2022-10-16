# Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program,
# który wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak
# najwięcej aut. Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.

# f(i, l, r) - samochody od indeksu 0 do i włącznie, mając długość l lewego pasa i długość r prawego pasa
# f(i, l, r) = f(i - 1, l - a[i], r) or f(i - 1, l, r - a[i])
# kolejność implementacji F[i][l][r]

def GetSolution(curr_car,L,R,t,res,left,right):
    if curr_car == 0:
        if L - t[0] >= 0: return left + [0], right
        else: return left,right + [0]

    if L - t[curr_car] >= 0 and res[curr_car-1][L-t[curr_car]][R]:
        return GetSolution(curr_car-1,L-t[curr_car],R,t,res,left + [curr_car],right)
    if R - t[curr_car] >= 0 and res[curr_car-1][L][R-t[curr_car]]:
        return GetSolution(curr_car-1,L,R-t[curr_car],t,res,left ,right + [curr_car])
    return left, right

def loading_ship(t,lenght):
    n = len(t)
    res = [[[False for _ in range(lenght+1)] for _ in range(lenght+1)] for _ in range(n)]

    res[0][t[0]][0] = True
    res[0][0][t[0]] = True

    for i in range(1, n):
        for left in range(lenght+1):
            for right in range(lenght+1):
                put_on_left = res[i-1][left - t[i]][right] if left - t[i] >= 0 else False
                put_on_right = res[i-1][left][right-t[i]] if right - t[i] >= 0 else False
                res[i][left][right] = put_on_left or put_on_right

    car ,l , r = 0,0,0
    for i in range(n):
        for left in range(lenght+1):
            for right in range(lenght+1):
                if res[i][left][right]:
                    car = i
                    l = left
                    r = right
                    break
    return GetSolution(car,l,r,t, res, [], [])

test = [1, 4, 5, 4]
print(loading_ship(test, 8))
