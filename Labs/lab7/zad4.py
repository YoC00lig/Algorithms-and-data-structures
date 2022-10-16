# Zadanie 4. (wieże) Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko
# ma klocki różnej wysokości. Pierwsze dziecko ma klocki o wysokościach w1, . . . , w1 , drugie dziecko klocki o 1 n1
# wyskościach w2, . . . , w2 , itd. Dzieci właśnie poszły zjeść deser zanim ułożą swoje wieże, ale jedno dziecko 1 n2
# zostało. Ma teraz jedyną okazję, żeby podebrać kilka klocków innym dzieciom tak, żeby jego wieża była najwyższa.
# Proszę podać możliwie najszybszy algorytm rozwiązujący ten problem, który zabiera minimalną ilość klocków.
# (Proszę zwrócić uwagę, że liczby wji mogą być bardzo duże.)

def tower(T):
    n = len(T)
    sums = []
    cnt = curr = 0
    # sums przechowuje wysokość klocków każdego dziecka
    # sortuje klocki każdego dziecka
    for i in range(n):
        sums.append(sum(T[i]))
        T[i].sort()
    # dopóki wieża nie jest największa, to podbieramy największy klocek
    # dziecka, które ma aktualnie największą wieżę
    while curr < max(sums):
        cnt += 1
        ind = sums.index(max(sums))
        height = T[ind].pop()
        curr += height
        sums[ind] -= height

    return cnt

