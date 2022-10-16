# Given an array of non-negative integers arr, you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
#
# Notice that you can not jump outside of the array at any time.


#Example 1:
#Input: arr = [4,2,3,0,3,1,2], start = 5
#Output: true
#Explanation:
#All possible ways to reach at index 3 with value 0 are:
#index 5 -> index 4 -> index 1 -> index 3
#index 5 -> index 6 -> index 4 -> index 1 -> index 3

#Example 2:
#Input: arr = [4,2,3,0,3,1,2], start = 0
#Output: true
#Explanation:
#One possible way to reach at index 3 with value 0 is:
#index 0 -> index 4 -> index 1 -> index 3

#Example 3:
#Input: arr = [3,0,2,1,2], start = 2
#Output: false
#Explanation: There is no way to reach at index 1 with value 0.

# SOLUTION:
# Tworzę listę sąsiedztwa O(n)
# Następnie przechodzę przez graf BFS i jeśli spotkam indeks, pod którym w tablicy arr
# występuje wartość 0 to zwracam True

from collections import deque
def canReach(arr,start):
    def BFS(graph, start):
        n = len(graph)
        visited = [False] * n
        q = deque([])
        visited[start] = True
        q.append(start)

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    if arr[v] == 0: return True
                    q.append(v)
        return False

    def PrepareNghlist(T):
        n = len(T)
        nl = [[] for _ in range(n)]

        for i in range(n):
            if i - T[i] >= 0:
                nl[i].append(i - T[i])
            if i + T[i] < n:
                nl[i].append(i + T[i])
        return nl

    nl = PrepareNghlist(arr)
    if arr[start] == 0: return True
    return BFS(nl, start)