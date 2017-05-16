from utility.graphs import *
import math
from heapq import heappush, heappop

"""Shortest Path
Input: A graph G with non-negative edge
weights, a source vertex s and a target vertex t.

Output: The shortest path between s an t in G
"""


"""Reversed Graph
Reversed graph Gr for a graph G is the graph
with the same set of vertices V and the set of
reversed edges Er, such that for any (u,v) in E
there is an edge (v,u) in Er and vice versa.
"""


def bidirectional_dijkstra(G: Graph, s: int, t: int):
    """
    Bidirectional Dijkstra
    Running time: O((|E| + |V|)log|V|)
    Speedup in practice depends on the graph
    :param G: 
    :param s: 
    :param t: 
    :return: 
    """
    Gr = reverse_graph(G)
    dist = {}
    distr = {}
    prev = {}
    prevr = {}
    queue = []
    queuer = []
    for v in G.V.keys():
        if v == s:
            dist[v] = 0
            distr[v] = math.inf
        elif v == t:
            distr[v] = 0
            dist[v] = math.inf
        else:
            distr[v] = math.inf
            dist[v] = math.inf

        prev[v] = None
        prevr[v] = None
        heappush(queue, (dist[v], v))
        heappush(queuer, (distr[v], v))

    proc = set()
    procr = set()

    while True:
        v = heappop(queue)[1]
        process(v, G, dist, prev, proc, queue)

        if v in procr:
            return shortest_path(s, dist, prev, proc, t, distr, prevr, procr)

        vr = heappop(queuer)[1]
        process(vr, Gr, distr, prevr, procr, queuer)


def process(v: int, G: Graph, dist: dict, prev: dict, proc: set, queue: list):
    for u in G.V[v].adj.keys():
        relax(v, u, G.V[v].adj[u], dist, prev, queue)
    proc.add(v)


def relax(u, v, uv, dist: dict, prev: dict, queue: list):
    if dist[v] > dist[u] + uv :
        dist[v] = dist[u] + uv
        prev[v] = u
        heappush(queue, (dist[v], v))


def shortest_path(s, dist: dict, prev: dict, proc: set, t, distr: dict, prevr: dict, procr: set):
    distance = math.inf
    u_best = None
    for u in proc.union(procr):
        if dist[u] + distr[u] < distance:
            u_best = u
            distance = dist[u] + distr[u]
    path = []
    last = u_best
    while last != s:
        path.append(last)
        last = prev[last]
    path.reverse()
    last = u_best
    while last != t:
        last = prevr[last]
        path.append(last)

    return distance, path

if __name__ == '__main__':
    G = Graph()
    G.V[0] = Vertex.with_adj_vertices({1: 3, 5: 10})
    G.V[1] = Vertex.with_adj_vertices({2: 3, 4: 5, 5: 8})
    G.V[2] = Vertex.with_adj_vertices({3: 2, 4: 1, 5: 3})
    G.V[3] = Vertex.with_adj_vertices({})
    G.V[4] = Vertex.with_adj_vertices({3: 0})
    G.V[5] = Vertex.with_adj_vertices({1: 2, 4: 4})

    dist, path = bidirectional_dijkstra(G, 0, 3)
    print(dist, path)