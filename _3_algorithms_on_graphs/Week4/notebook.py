import math
from heapq import heappush, heappop
from utility.graphs import Graph, Vertex


def dijkstra(G: Graph, S: int):
    """Dijkstra Algorithm
    Running time: O((|E| + |V|)log|V|)
    :param G:
    :param S:
    :return:
    """
    dist = {}   # type: dict
    prev = {}   # type: dict
    queue = []
    processed = set()
    for v in G.V.keys():
        dist[v] = 0 if v == S else math.inf
        prev[v] = None
        heappush(queue, (dist[v], v))

    while len(queue) != 0:
        u = heappop(queue)  # type: Vertex
        if u[1] not in processed:
            for v in G.V[u[1]].adj.keys():
                if dist[v] > dist[u[1]] + G.V[u[1]].adj[v]:
                    dist[v] = dist[u[1]] + G.V[u[1]].adj[v]
                    prev[v] = u[1]

                    #Change priority
                    heappush(queue, (dist[v], v))
        processed.add(u[1])
    print(dist)


'''Bellman-Ford Algorithm
xy -> max == log(x) + log(y) -> max
'''


if __name__ == '__main__':
    G = Graph()
    G.V[0] = Vertex.with_adj_vertices({1: 3, 5: 10})
    G.V[1] = Vertex.with_adj_vertices({2: 3, 4: 5, 5: 8})
    G.V[2] = Vertex.with_adj_vertices({3: 2, 4: 1, 5: 3})
    G.V[3] = Vertex.with_adj_vertices({})
    G.V[4] = Vertex.with_adj_vertices({3: 0})
    G.V[5] = Vertex.with_adj_vertices({1: 2, 4: 4})
    dijkstra(G, 0)