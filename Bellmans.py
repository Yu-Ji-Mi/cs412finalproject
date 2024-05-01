import sys

def longest_path(graph, vertices, edges):
    # Initialize distance array
    dist = [-sys.maxsize - 1] * vertices
    dist[0] = 0

    # Relax all edges |V| - 1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float("-Inf") and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w

    # Return the longest path
    return dist

# Test case
vertices = 3
edges = [(0, 1, 3), (1, 2, 4), (0, 2, 5)]
graph = longest_path({}, vertices, edges)
print(max(graph), [i for i, x in enumerate(graph) if x == max(graph)])
