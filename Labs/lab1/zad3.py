"""
Zadanie 3. (złożoność sortowania prostego) Proszę omówić złożoność obliczeniową sortowań pro-
stych:

1. jaka jest złożoność najlepszego i najgorszego przypadku?
2. ile przypisań i ile porównań wykonuje dany algorytm (jak poprawić sortowanie przez wstawianie?)
3. która z metod wolnych jest stabilna (i co to znaczy, że sortowanie jest stabilne)?

"""

# ad 1
# Bubble-sort: best O(n^2) worst O(n^2)
# Selection-sort: best O(n^2) worst O(n^2)
# Insertion-sort: best O(n) worst O(n^2)



# ad 3
# Sortowanie jest stabilne jeśli wzajemna kolejnośc elementów o tych samych kluczach
# pozostaje niezmieniona na skutek sortowania.
# Sortowaniami stabilnymi są bubble-sort i insertion-sort
# selection-sort nie jest stabilne
