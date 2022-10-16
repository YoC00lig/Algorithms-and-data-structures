# Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n),
# który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.

#-----ROZWIĄZANIE-----
# W rozwiązaniu zadania skorzystam z algorytmu wyszukiwania lidera.
# Algorytm ten bazuje na zależności, że jeśli z tablicy usuniemy elementy które mają różne wartości,
# to nawet jeśli któryś z nich był liderem to jego status lidera w tablicy pozostanie nienaruszony.
# Na początku przyjmuję pierwszy element z tablicy jako kandydata na lidera. Następnie iteruję przez całą tablicę.
# Jeśli kolejny element ma wartość inną niż aktualny kandydat, oznacza to sytuację że usunęliśmy dwie różne wartości.
# Licznik zmniejszamy o 1. Jeśli zaś kolejny element jest równy kandydatowi
# to zwiększamy licznik o 1. Jeśli nasz licznik jest równy zero to musimy przyjąć jakiegoś nowego kandydata na lidera.

def FindLeader(T):
    n = len(T)
    cnt = 1
    leader = T[0]
    for i in range(1, n):
        if T[i] == leader: cnt += 1
        elif cnt != 0 and T[i] != leader: cnt -= 1
        elif cnt == 0:
            leader = T[i]
            cnt = 1
    if cnt > 0: return leader
    return None