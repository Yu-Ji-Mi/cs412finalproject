import heapq


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
    return dist


def main():
    nodes = set()
    adj_list = {}
    n, m = input().split()
    for _ in range(int(m)):
        u, v, w = input().split()
        w = float(w)
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
    print(lp_dijkstras(adj_list, 'a', dist, pred))


if __name__ == "__main__":
    main()
