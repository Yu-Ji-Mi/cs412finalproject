from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.longest_path_length = 0
        self.longest_path = []

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dfs(self, node, visited, path, length, look_ahead):
        visited.add(node)
        path.append(node)

        if length > self.longest_path_length:
            self.longest_path_length = length
            self.longest_path = path.copy()

        if look_ahead > 0:
            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited, path, length + weight, look_ahead - 1)

        path.pop()
        visited.remove(node)

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        vertices, edges_count = map(int, lines[0].split())
        edges = []
        for line in lines[1:]:
            u, v, w = line.split()
            edges.append((u, v, int(w)))
        return vertices, edges

# Test case
vertices, edges = read_graph_from_file('graph.txt')
g = Graph()
for u, v, w in edges:
    g.add_edge(u, v, w)

look_ahead = 2  # Modify this parameter as needed
g.dfs('a', set(), [], 0, look_ahead)

print(g.longest_path_length)
print(' '.join(g.longest_path))
