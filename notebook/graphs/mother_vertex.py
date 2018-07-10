"""
A mother vertex in a graph G = (V,E) is a vertex v such 
that all other vertices in G can be reached by a path from v.
"""

g = {
    '0': ['3', '2'],
    '1': ['0'],
    '2': ['1'],
    '3': ['4'],
    '4': []
}


def explore(g, v, visited):
    if v in visited:
        return 

    visited.add(v)
    for _v in g[v]:
        explore(g, _v, visited)


def mother_vertex(g: dict):
    visited = set()
    last_v = None

    for v in g.keys():
        if v not in visited:
            explore(g, v, visited)
            last_v = v

    visited.clear()
    explore(g, last_v, visited)
    if all(v in visited for _v in g.keys()):
        return last_v
    return -1

print('Mother vertex = ', mother_vertex(g))
