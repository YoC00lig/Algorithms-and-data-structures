# Dana jest tablica A zawierająca n parami różnych liczb.
# Proszę zaproponować algorytm, który znajduje takie dwie liczby
# x i y z A, że y−x jest jak największa oraz w tablicy nie ma żadnej
# liczby z takiej, że x < z < y (innymi słowy, po posortowaniu tablicy A
# rosnąco wynikiem byłyby liczby A[i] oraz A[i + 1] dla których A[i + 1] − A[i] jest największe).

#ROZWIĄZANIE
# Do rozwiązania problemu wykorzystam Bucket sort.
# Największą różnicę wyznaczy maximum i minimum z dwóch najbardziej oddalonych od siebie kubełków.
# Zeby znaleźć tę różnicę stworzę dwa wskaźniki - jeden będzie wskazywał na ostatni odwiedzony niepusty kubełek,
# kolejnym będę iterować przez całą tablicę kubełków, aż do znalezienia następnego w kolei niepustego kubełka.
# Wtedy obliczamy maxymalny dystans jako różnicę maksymalnej liczby w kubełku wskazywanym przez
# first oraz minimalnej liczby w kubełku wskazywanym przez drugi wskaźnik.
# W posortowanej tablicy byłyby to liczby które stoją obok siebie.

def MaxDifference(T):
    n = len(T)
    mini = min(T)
    maxi = max(T)
    interval = (maxi-mini)/ n
    buckets = [[] for _ in range(n)]
    for val in T:
        index = int((val-mini)/interval) if int((val-mini)/interval) < n else n-1
        buckets[index].append(val)

    first = 0
    for i in range(n):
        if buckets[i] != []:
            first = i
            break

    dist = 0
    num1,num2 = 0, 0
    for i in range(first+1, len(T)):
        if buckets[i] != []:
            dist = max(min(buckets[i])-max(buckets[first]),dist)
            if dist == min(buckets[i])-max(buckets[first]):
                num1,num2 = max(buckets[first]), min(buckets[i])
            first = i
    return dist, num1, num2

print(MaxDifference([3,8,1,4,2]))
