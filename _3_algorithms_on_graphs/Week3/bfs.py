import math

G = {'A': ['B', 'S'],
     'B': ['A', 'C', 'H', 'G'],
     'C': ['B', 'S'],
     'D': ['E', 'F'],
     'E': ['S', 'D'],
     'F': ['D', 'G'],
     'G': ['F', 'H', 'D'],
     'H': ['B', 'G'],
     'S': ['A', 'E', 'D', 'C']}


def shortest_path(g: dict, a: str, b: str, path: list = []):
    q = []
    dist = dict()
    prev = dict()

    q.append(a)
    dist[a] = 0

    while q:
        v = q.pop()
        for n in g[v]: # type: str
            if n not in dist:
                q.append(n)
                dist[n] = dist[v] + 1
                prev[n] = v

    return dist, prev


def reconstruct_path(s: str, u: str, prev: dict):
    result = []
    while u != s:
        result.append(u)
        u = prev[u]
    result.append(u)
    return result[::-1]


dist, prev = shortest_path(G, 'S', 'A', [])
print(dist)
print(reconstruct_path('S', 'F', prev))