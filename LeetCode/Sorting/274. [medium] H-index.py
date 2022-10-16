"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.
"""

# O(n) - counting sort

def hIndex(citations):
    n = len(citations)
    maxi = max(citations) + 1
    tab = [0 for i in range(maxi)]

    for i in range(n):
        tab[citations[i]] += 1

    ind = maxi - 1
    while ind - 1 >= 0:
        tab[ind - 1] += tab[ind]
        ind -= 1
    for i in range(maxi - 1, -1, -1):
        if tab[i] >= i:
            return i