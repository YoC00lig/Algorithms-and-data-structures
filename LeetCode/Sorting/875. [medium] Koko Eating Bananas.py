"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

from math import ceil
def minEatingSpeed(piles,h):
    n = len(piles)

    # funkcja zwraca wartość True jeśli koko jest w stanie zjeść wszystkie banany w ciągu h
    # godzin jedząc po x bananów na godzinę
    def CanEat(x):
        hours = 0
        for pile in piles:
            hours += ceil(pile / x)
        if hours <= h:
            return True
        return False

    left = 1
    right = max(piles)
    mini = 0
    while left <= right:
        mid = (left + right) // 2
        if CanEat(mid):
            right = mid - 1
            mini = mid
        if not CanEat(mid):
            left = mid + 1

    return mini