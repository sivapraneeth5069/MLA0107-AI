class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, node1, node2):
        self.graph.setdefault(node1, []).append(node2)
        self.graph.setdefault(node2, []).append(node1)
    def graph_coloring(self):
        colors = {}
        colored_nodes = set()
        for node in self.graph:
            available_colors = set(range(1, len(self.graph) + 1))
            for neighbor in self.graph[node]:
                if neighbor in colors:
                    available_colors.discard(colors[neighbor])
            if available_colors:
                color = min(available_colors)
                colors[node] = color
                colored_nodes.add(node)
            else:
                raise ValueError("No valid coloring exists.")
        return colors
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'A')
g.add_edge('A', 'C')
coloring = g.graph_coloring()
print("Node colors:", coloring)
