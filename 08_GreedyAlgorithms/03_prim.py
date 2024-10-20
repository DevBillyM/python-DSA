# Prim's Algorithm for Minimum Spanning Tree (MST) using Priority Queue

import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        pq = [(0, 0)]  # (weight, vertex)
        mst_set = [False] * self.V
        total_weight = 0

        while pq:
            weight, u = heapq.heappop(pq)

            if mst_set[u]:
                continue

            total_weight += weight
            mst_set[u] = True

            for v, w in self.graph[u]:
                if not mst_set[v]:
                    heapq.heappush(pq, (w, v))

        return total_weight

# Testing Prim's Algorithm
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Total weight of MST:", g.prim_mst())  # Output: Total weight of MST: 19
