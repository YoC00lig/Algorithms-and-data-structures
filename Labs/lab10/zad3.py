# Zadanie 1. (SAT-2CNF) Dana jest formuła logiczna w postaci 2CNF. To znaczy, że formuła jest koniunkcją
# klauzuli, gdzie każda klauzula to alternatywa dwóch literałów, a każdy literał to zmienna lub jej negacja.
# Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest:
# (x ∨ y) ∧ (x ∨ z) ∧ (z ∨ y).
# Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartościowanie spełniające
# formułę.

# x v y jest równoważne -x => y oraz -y => x
# x V z jest równoważne -x => z oraz -z => x
# z v y jest równoważne -z => y oraz -z => y

# Tworzymy graf składający się z 2 * liczba zmiennych (zmienna i jej zaprzeczenie).
# (-x => y oznacza krawędź skierowaną z -x do y)
# w tak powstałym grafie szukam spójnych składowych
