import networkx as nx
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(path1=None, path2=None):
    G = nx.DiGraph()

    # open the file
    with open('graph.txt', 'r') as file:
        # read number of vertices and edges
        n, m = map(int, file.readline().split())

        # read edges
        for _ in range(m):
            u, v, w = file.readline().split()
            G.add_edge(u, v, weight=int(w))

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # highlight the first path if it is given
    if path1 is not None:
        # nx.draw_networkx_labels(G, pos, labels={node: node for node in path1}, font_color='r')
        edges = [(path1[i-1], path1[i]) for i in range(1, len(path1))]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)

    # highlight the second path if it is given
    if path2 is not None:
        edges = [(path2[i-1], path2[i]) for i in range(1, len(path2))]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='b', width=2)

    plt.show()


# specify the path to be highlighted
path = ['a', 'x', 'm', 'l', 'k', 'c']
path2 = ['a', 'x', 'i', 'v', 'b', 'u', 'l', 'k', 'c']
draw_graph(path, path2)

