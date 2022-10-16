# (maximin) Rozważmy ciąg (a0,...,an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0,...,al1), (al1+1,...,al2),...,(alk1+1,...,an−1).
# Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg
# rozumiemy podciąg o najmniejszej wartości (rozstrzygając remisy w dowolny sposób).
# Wartością podziału jest wartość jego najgorszego podciągu. Zadanie polega na znalezienie
# podziału ciągu (a0,...,an−1) o maksymalnej wartości.

# dp[i][k] - maksymalna wartość ciągu do i-tego elementu w tablicy przy k podziałach
def find_division(A, k):
    if k <= 0: return 0
    n = len(A)
    dp = [[0] * (k+1) for _ in range(n)]
    # jeśli mamy tylko 1 podział, to będzie on wynosił tyle, co suma wszystkich elementów
    dp[0][1] = A[0]
    for i in range(1, n):
        dp[i][1] = dp[i-1][1] + A[i]
    # zapisuje sumę elementów do indeksu i
    S = [0] * n
    S[0] = A[0]
    for i in range(1, n):
        S[i] = S[i-1] + A[i]

    for i in range(1, n): # sprawdzamy do i-tego elementu w tablicy
        for j in range(2, k+1): # k - ilość podziałów
            for m in range(i+1):
                # do i-m elementu był ostatni podział, od i-m jest następny
                val1, val2 = dp[i-m][j-1], S[i] - S[i-m]
                dp[i][j] = max(dp[i][j], min(val1, val2))

    return dp[n-1][k]


