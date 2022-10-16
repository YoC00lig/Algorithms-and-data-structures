# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a,b].
# Dany jest ciąg klocków [a1,b1], [a2,b2], ..., [an,bn]. Klocki spadają
# na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować algorytm,
# który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny
# spadajacy klocek mieścił się w całości w tam, który spadł tuż przed nim.

# f(i) - jakiej długości  ciąg klocków możemy utworzyć do i-tego indeksu

def inclusion(kl1,kl2): # czy kl2 zawiera się w kl1?
    if kl1[0] <= kl2[0]:
        if kl1[1] >= kl2[1]:
            return True
    return False

def tower(t):
    n = len(t)
    res = [1 for _ in range(n)]
    if inclusion(t[0], t[1]):
        res[1] = 2
    for i in range(2,n):
        for j in range(i-1,-1,-1):
            if inclusion(t[j],t[i]) and res[j] + 1 > res[i]:
                res[i] = res[j] + 1

    return n - max(res)
