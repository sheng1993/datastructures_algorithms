import _3_algorithms_on_graphs.Week1.notebook as graph
import math


def bfs(G: graph.Graph, S: graph.Vertex):
    dist = [math.inf] * len(G.vertices)
    prev = [None] * len(G.vertices)
    dist[S] = 0
    Q = [S]
    while len(Q) != 0:
        u = Q.pop(0)
        for n in u.adj: # type: graph.Vertex
            if dist[n] == math.inf:
                Q.append(n)
                dist[n] = dist[u] + 1
                prev[n] = n
