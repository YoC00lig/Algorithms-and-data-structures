# Zadanie 8. (wędrówka po szachownicy)
# Dana jest szachownica A o wymiarach n × n. Szachownica zawiera
# liczby wymierne. Należy przejść z pola (1,1)  na pole (n,n)
# korzystając jedynie z ruchów “w dół” oraz “w prawo”. Wejście
# na dane pole kosztuje tyle, co znajdująca się tam liczba.
# Proszę podać algorytm znajdujący trasę o minimalnym koszcie.

# najpierw sumuje po kolei pierwszą kolumnę i pierwszy wiersz, potem na bieżąco wybieram
# w którą stronę się poruszyć tak,żeby wyszedł jak najmniejszy koszt

def MinimumCostPath(costs):
    n = len(costs)
    for i in range(2,n): costs[0][i] += costs[0][i-1]
    for i in range(2,n): costs[i][0] += costs[i-1][0]
    for i in range(2,n):
        for j in range(2,n):
            costs[i][j] = min(costs[i-1][j], costs[i][j-1]) + costs[i][j]
    return costs[-1][-1]