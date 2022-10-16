"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


"""

from collections import defaultdict, Counter

def findItinerary(tickets):
    def epath(pairs):
        G = defaultdict(list)
        dout, din = Counter(), Counter()
        for u, v in pairs:
            G[u].append(v)
            dout[u] += 1
            din[v] += 1

        for u in G: G[u].sort(reverse=True)
        s = "JFK"

        result = []

        def DFS(u):
            while dout[u]:
                dout[u] -= 1
                v = G[u][dout[u]]
                DFS(v)
            result.append(u)

        DFS(s)
        result.reverse()
        return result

    return epath(tickets)