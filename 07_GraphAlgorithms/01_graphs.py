# Graph Representation using Adjacency List

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display_graph(self):
        for node, edges in self.graph.items():
            print(f"{node} -> {', '.join(map(str, edges))}")

# Testing Graph Representation
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.display_graph()
