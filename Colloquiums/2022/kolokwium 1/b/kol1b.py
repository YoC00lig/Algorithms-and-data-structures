from kol1btesty import runtests

# słowa wkładam do bucketu odpowiadającego długosci słowa
# w każdym buckecie z osobna sprawdzam ilość anagramów

def CheckAnagrams(s1,s2):
    cnt = [0] * 27
    for i in s1:
        cnt[ord(i)-97] += 1
    for i in s2:
        cnt[ord(i)-97] -= 1
    for i in cnt:
        if i != 0:
            return False
    return True

def GetAns(bucket, curr_word):
    cnt = 0
    t = []
    for word in bucket:
        if CheckAnagrams(word, curr_word):
            t.append(word)
            cnt += 1
    for word in t: bucket.remove(word)
    # jeśli te słowa zostały już sprawdzone, to nie ma sensu sprawdzać ich jeszcze raz
    # bo nie będą już należeć do zbioru anagramów innego słowa, bo gdyby należały, to to słowo znalazłoby się też w tablicy t
    return cnt



def f(T):
    maxi = None # długość najdłuzszego stringa
    n = len(T)
    for i in range(n):
        if maxi is None or len(T[i]) > maxi:
            maxi = len(T[i])

    buckets = [[] for _ in range(maxi + 1)]
    for i in range(n):
        index = len(T[i])
        buckets[index].append(T[i])

    max_amount = 0

    for bucket in buckets:
        if len(bucket) > 1:
            for word in bucket:
                x = word
                a = GetAns(bucket, x)
                if a > max_amount: max_amount =a


    return max_amount


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True)
