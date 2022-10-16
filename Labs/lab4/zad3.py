# roszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n,
# każde nad alfabetem długości k, sprawdza czy A i B są swoimi anagramami.

# 1. Proszę zaproponować rozwiązanie działające w czasie O(n + k).
# 2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo
# większe od n—np. dla alfabetu unicode; złożoność pamięciowa może być rzędu O(n + k)).

# Proszę zaimplementować oba algorytmy.

# ROZWIĄZANIE AD 1
# W algorytmie na początku wyszukujemy wartości maksymalnej i minimalnej znaków unicode znajdujących się w obydwu słowach.
# następnie tworzymy tablicę Counter w której przechowujemy ile razy pojawił się znak.
# Na początku iterujemy przez pierwsze słowo i zwiększamy dla każdego znaku jego odpowiednik w tablicy counter.
# Następnie iterujemy przez drugie słowo i zmniejszamy wartośc w tablicy Counter.
# Jeśli w obydwu słowach wystąpiły te same znaki, to wartość każdego elementu w tablicy counter powinna być równa zero
# . Jeśli nie jest, to znaczy że znaki nie były te same

def minimax(string):
    mini = maxi = string[-1]
    for i in range(1,len(string),2):
        if string[i] > string[i-1]:
            if string[i-1] < mini:
                mini = string[i-1]
            if string[i] > maxi:
                maxi = string[i]
        else:
            if string[i] < mini:
                mini = string[i]
            if string[i-1] > maxi:
                maxi = string[i-1]
    return mini,maxi

def CheckAnagrams1(s1,s2):
    if len(s1) != len(s2):
        return False

    mini1,maxi1 = minimax(s1)
    mini2,maxi2 = minimax(s2)
    miniord = min(ord(mini1),ord(mini2))
    maxiord = max(ord(maxi1),ord(maxi2))

    counter = [0] * (maxiord-miniord+1)
    for char in s1:
        counter[ord(char)-miniord] += 1
    for char in s2:
        counter[ord(char) - miniord] -= 1

    for i in counter:
        if i != 0:
            return False
    return True

# ROZWIĄZANIE AD 2
# W podejściu drugim nie interesuje nas zużycie pamięci. Wobec tego możemy zaalokować sobie tablicę,
# która będzie zawierała odpowiednik każdego znaku z unicode i operować na niej, zamiast na tablicy Counter
# jak w pierwszym podpunkcie.

def CheckAnagrams2(s1,s2):
    if len(s1) != len(s2):
        return False
    counter = [0 for _ in range(2**16)]
    for i in range(len(s1)):
        counter[ord(s1[i])] += 1
        counter[ord(s2[i])] -= 1
    for i in range(len(s1)):
        if counter[ord(s1[i])] != 0 or counter[ord(s2[i])] != 0:
            return False
    return True