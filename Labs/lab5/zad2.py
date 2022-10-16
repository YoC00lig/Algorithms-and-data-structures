# Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. Proszę podać
# i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A,
# które sumują się do zadanej wartości T.

# F(i,j) - czy ciąg kończący się na indeksie i sumuje się do j
# Złożoność czasowa O (n*target)

def SubsetSumProblem(T, target):
    n = len(T)
    matrix = [[False for _ in range(target+1)] for _ in range(n)]

    for i in range(n):
        if T[i] <= target:
            matrix[i][T[i]] = True
            if T[i] == target:
                return True

    for i in range(1, n):
        for j in range(T[i], target+1):
            if j-T[i] >= 0 and matrix[i-1][j-T[i]]:
                matrix[i][j] = True
                if j == target:
                    return True
    return False

T = [6,3,2,1,3,5,2,4,2]
print(SubsetSumProblem(T,22))