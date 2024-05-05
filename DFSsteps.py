from collections import defaultdict
import time
from printgraph import draw_graph
from drawtiming import drawtimingplot
# Builds a graph and calls the Lookahead.


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.longest_path_length = 0
        self.longest_path = []

    # creates edges
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dfs(self, node, visited, path, length, look_ahead):
        visited.add(node)
        path.append(node)

        # Update the longest path
        if length > self.longest_path_length:
            self.longest_path_length = length
            self.longest_path = path.copy()

        # recursively visit all the neighbors
        for neighbor, weight in self.graph[node]:
            # if the neighbor is not visited, visit it
            if neighbor not in visited:
                # if look_ahead is greater than 0, then call lookahead
                if look_ahead > 0:
                    temp_length = self.lookahead(
                        neighbor, visited, look_ahead - 1, weight)
                    # if the length of the path is greater than the longest path, then call dfs
                    if temp_length + length > self.longest_path_length:
                        self.dfs(neighbor, visited, path,
                                 length + weight, look_ahead)
                else:
                    # if look_ahead is 0, then call dfs
                    self.dfs(neighbor, visited, path,
                             length + weight, look_ahead)
        # backtrack
        path.pop()
        visited.remove(node)

    def lookahead(self, node, visited, look_ahead, length):
        # if look_ahead is 0 or the node has no neighbors, return the length
        if look_ahead == 0 or not self.graph[node]:
            return length
        # recursively visit all the neighbors
        max_length = -1
        for neighbor, weight in self.graph[node]:
            if neighbor not in visited:
                # is the temp_length greater than the max_length?
                temp_length = self.lookahead(
                    neighbor, visited, look_ahead - 1, length + weight)
                max_length = max(max_length, temp_length)
        return max_length


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
g_file = 'inputs/graphlarge.txt'
vertices, edges = read_graph_from_file(g_file)
g = Graph()
for u, v, w in edges:
    g.add_edge(u, v, w)
timings = []
for look_ahead in range(1, 10):  # Ranges of lookahead
    g.longest_path_length = 0
    g.longest_path = []
    start_time = time.time()
    g.dfs('a', set(), [], 0, look_ahead)
    end_time = time.time()
    print(f"Look Ahead: {look_ahead} Node(s)")
    print(f"Time: {end_time - start_time} seconds")
    timings.append(end_time - start_time)
    print(g.longest_path_length)
    # print the longest path in this format a b c d e
    print(" ".join(g.longest_path) + "\n")
    longest_path = g.longest_path

draw_graph(g_file, longest_path)
drawtimingplot(timings)
