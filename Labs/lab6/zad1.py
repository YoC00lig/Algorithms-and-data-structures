# Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii.
# Las składa się z n drzew rosnących na pozycjach 0,...,n−1.
# Dla każdego i ∈ {0,...,n−1} znany jest zysk ci, jaki można osiągnąć ścinając
# drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych drzew,
# ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm,
# dzięki któremu John znajdzie optymalny plan wycinki.


def black_forest(profits):
    n = len(profits)
    func = [0] * n
    func[0] = profits[0]
    func[1] = max(profits[0], profits[1])
    for i in range(2, n):
        func[i] = max(func[i - 1], func[i - 2] + profits[i])
    return func[n - 1]
