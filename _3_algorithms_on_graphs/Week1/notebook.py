class Vertex:
    def __init__(self):
        self.adj = []   # type: list
        self.visited = False
        self.cc = None  # connected component


class Graph:
    def __init__(self):
        self.vertices = []  # type: list


def pre_visit(v: Vertex):
    pass


def post_visit(v: Vertex):
    pass


def explore(v: Vertex, cc=None):
    v.visited = True
    pre_visit(v)
    if cc is not None:
        v.cc = cc
    for n in v.adj:     # type: Vertex
        if not n.visited:
            explore(n)
    post_visit(v)


def dfs(graph: Graph):
    for v in graph.vertices:    # type: Vertex
        v.visited = False
    cc = 1
    for v in graph.vertices:    # type: Vertex
        if not v.visited:
            explore(v, cc=cc)
            cc += 1