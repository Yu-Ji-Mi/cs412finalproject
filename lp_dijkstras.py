import heapq
from collections import deque


def lp_dijkstras(G, s, dist, pred):
    dist[s] = 0
    q = [(0, s)]
    while q:
        u = heapq.heappop(q)[1]
        for v in G[u]:
            # If edge is tense
            if dist[u] + G[u][v] < dist[v]:
                # Relax edge
                dist[v] = dist[u] + G[u][v]
                pred[v] = u
                heapq.heappush(q, (dist[v], v))
    # Compute Longest Path
    min_value = min(dist.values())
    return [(result, min_value) for result in dist if dist[result] == min_value]


def main():
    nodes = set()
    adj_list = {}
    n, m = input().split()
    for _ in range(int(m)):
        u, v, w = input().split()
        w = int(w)
        if u not in adj_list:
            adj_list[u] = {v: -w}
        else:
            adj_list[u][v] = -w
        nodes.add(u)
        nodes.add(v)
    for node in nodes:
        if node not in adj_list.keys():
            adj_list[node] = {}
    # init sssp
    dist = {node: float('inf') for node in nodes}
    pred = {node: None for node in nodes}
    # Run algorithm on all nodes
    maxpath = [(None, 0)]
    stack = deque()
    for node in nodes:
        result = lp_dijkstras(adj_list, node, dist, pred)
        # Add newest lp to the stack
        if result[0][1] < maxpath[0][1]:
            maxpath = result
            stack.append(
                f"{node} -> {maxpath[0][0]} (Length {-maxpath[0][1]})")
    # Result
    print(f"The Longest Path is {stack.pop()}")


if __name__ == "__main__":
    main()
