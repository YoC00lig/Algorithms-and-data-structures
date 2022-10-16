# Zadanie 2. (wybór zadań z terminami) Mamy dany zbiór zadań T = {t1, . . . , tn}.
# Każde zadanie ti dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna)
# oraz (b) zysk g(ti) za wykonanie w terminie (liczba naturalna). Wykonanie każdego
# zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie wykonane przed przekroczeniem
# swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane zadanie jest
# wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie
# i który prowadzi do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.


from bisect import bisect_left

# weighted job scheduling
def jobScheduling(S,E,profit):
    jobs = sorted(list(zip(S, E, profit)))
    S = [i[0] for i in jobs]
    n = len(jobs)
    dp = [0] * (n + 1)
    for k in range(n - 1, -1, -1):
        temp = bisect_left(S, jobs[k][1])
        dp[k] = max(jobs[k][2] + dp[temp], dp[k + 1])
    return dp[0]

